# .\.venv\Scripts\Activate.ps1
# pip freeze > requirements.txt

from audio.microphone import Microphone
from audio.speaker import Speaker
from commands.detector import CommandDetector
from ai.ollama import Ollama
from agenda.manager import AgendaManager
from face.recognizer import FaceRecognizer

# =====================================================
# INICIALIZAÇÃO
# =====================================================
print("Inicializando AlexaBot...")

microphone = Microphone()
speaker = Speaker()
commands = CommandDetector()
ollama = Ollama()
agenda = AgendaManager()
face_recognizer = FaceRecognizer()

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
    # ENTRADA DO USUÁRIO
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
    # NORMALIZA ENTRADA DO USUÁRIO
    # -------------------------------------------------
    texto = commands.normalize(texto)

    # -------------------------------------------------
    # FALA SEM WAKE WORD
    # -------------------------------------------------
    if not commands.has_wake_word(texto):
        print("Fala ignorada.")
        continue

    # -------------------------------------------------
    # REMOVE WAKE WORD
    # -------------------------------------------------
    texto = commands.remove_wake_word(texto)

    # -------------------------------------------------
    # ENCERRAR CONVERSA
    # -------------------------------------------------
    if commands.is_exit_command(texto):
        resposta = "Até mais!"
        print("Alexa:", resposta)
        speaker.speak(resposta)
        break

    # ================================================= 
    # CADASTRAR EVENTO NA AGENDA 
    # ================================================= 
    if commands.is_add_agenda_command(texto):
        resposta = "Ok, qual evento devo cadastrar?"
        print("Alexa:", resposta)
        speaker.speak(resposta)
        if microphone.enabled:
            evento = microphone.listen()
            if evento is None:
                print("Não consegui entender o evento.")
                resposta = "Não consegui entender o evento."
                speaker.speak(resposta)
                continue
        else:
            evento = input("\nDigite o evento: ")
        sucesso = agenda.adicionar_evento(evento)
        if sucesso:
            resposta = "Evento cadastrado com sucesso."
        else:
            resposta = "Não consegui cadastrar o evento."
        print("Alexa:", resposta)
        speaker.speak(resposta)
        continue

    # =================================================
    # LER AGENDA
    # =================================================
    if commands.is_read_agenda_command(texto):
        eventos = agenda.ler_eventos()
        # ---------------------------------------------
        # Agenda vazia
        # ---------------------------------------------
        if not eventos:
            resposta = "Sua agenda está vazia."
            print("Alexa:", resposta)
            speaker.speak(resposta)
            continue

        # ---------------------------------------------
        # Monta resposta com todos os eventos
        # ---------------------------------------------
        if len(eventos) == 1:
            resposta = (f"Você possui 1 evento cadastrado. O evento é: {eventos[0]}.")
        else:
            resposta = (
                f"Você possui {len(eventos)} eventos cadastrados. "
                "Os eventos são: "
                + ". ".join(
                    f"{numero}: {evento}"
                    for numero, evento in enumerate(eventos, start=1)
                )
                + "."
            )
        # ---------------------------------------------
        # Responde
        # ---------------------------------------------
        print("Alexa:", resposta)
        speaker.speak(resposta)
        continue

    # =================================================
    # LIMPAR AGENDA
    # =================================================
    if commands.is_clear_agenda_command(texto):
        eventos = agenda.ler_eventos()

        if not eventos:
            resposta = "Sua agenda já está vazia."
            print("Alexa:", resposta)
            speaker.speak(resposta)
            continue

        # ---------------------------------------------
        # Limpa os eventos
        # ---------------------------------------------
        sucesso = agenda.limpar_agenda()

        if sucesso:
            resposta = "Agenda limpa com sucesso."
        else:
            resposta = "Não consegui limpar a agenda."

        print("Alexa:", resposta)
        speaker.speak(resposta)
        continue

    # =================================================
    # RECONHECER FACE
    # =================================================

    if commands.is_face_recognition_command(texto):
        resposta = "Certo, vou verificar quem está na minha frente."
        print("Alexa:", resposta)
        speaker.speak(resposta)
        pessoa = face_recognizer.reconhecer()

        if pessoa is None:
            resposta = ("Não consegui reconhecer nenhuma pessoa.")

        elif pessoa == "Desconhecido":
            resposta = ("Não consegui identificar você.")

        else:
            resposta = (f"Você é {pessoa}.")

        print("Alexa:", resposta)
        speaker.speak(resposta)
        continue

    # -------------------------------------------------
    # ALEXA SEM COMANDO
    # -------------------------------------------------
    if not texto:
        resposta = "Pode falar, estou te ouvindo."
        print("Alexa:", resposta)
        speaker.speak(resposta)
        continue

    # -------------------------------------------------
    # FALLBACK PARA IA
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