from audio.microphone import Microphone
from audio.speaker import Speaker
from commands.detector import CommandDetector
from ai.ollama import Ollama

# =====================================================
# INICIALIZAÇÃO
# =====================================================
print("Inicializando AlexaBot...")

microphone = Microphone()
speaker = Speaker()
commands = CommandDetector()
ollama = Ollama()

# =====================================================
# VERIFICA DISPOSITIVOS
# =====================================================
voz_entrada = microphone.check()
voz_saida = speaker.check()

if voz_entrada:
    print("✓ Entrada de voz disponível.")
else:
    print("✗ Entrada de voz indisponível.")

if voz_saida:
    print("✓ Saída de áudio disponível.")
else:
    print("✗ Saída de áudio indisponível.")

# =====================================================
# LOOP PRINCIPAL
# =====================================================
while True:
    # -------------------------------------------------
    # ENTRADA
    # -------------------------------------------------
    if microphone.enabled:
        texto = microphone.listen()
        if texto is None:
            if not microphone.enabled:
                texto = input("\nVocê: ")
            else:
                continue
    else:
        texto = input("\nVocê: ")

    # -------------------------------------------------
    # NORMALIZA
    # -------------------------------------------------
    texto = commands.normalize(texto)

    # -------------------------------------------------
    # WAKE WORD
    # -------------------------------------------------
    if not commands.has_wake_word(texto):
        print("Fala ignorada.")
        continue

    # -------------------------------------------------
    # REMOVE WAKE WORD
    # -------------------------------------------------
    texto = commands.remove_wake_word(texto)

    # -------------------------------------------------
    # SAÍDA
    # -------------------------------------------------
    if commands.is_exit_command(texto):
        resposta = "Até mais!"
        print("Alexa:", resposta)
        speaker.speak(resposta)
        break

    # -------------------------------------------------
    # ALEXA SEM COMANDO
    # -------------------------------------------------
    if not texto:
        resposta = "Pode falar, estou te ouvindo."
        print("Alexa:", resposta)
        speaker.speak(resposta)
        continue

    # -------------------------------------------------
    # IA
    # -------------------------------------------------
    try:
        resposta = ollama.ask(texto)
        print(f"Alexa: {resposta} | Frase repassada: {texto}")
        speaker.speak(resposta)

    except ConnectionError:
        print("Erro: não foi possível conectar ao Ollama.")

    except RuntimeError as erro:
        print(erro)

    except Exception as erro:
        print(f"Erro inesperado: {erro}")