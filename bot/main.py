# .\.venv\Scripts\Activate.ps1

from gtts import gTTS 
from pygame import mixer 
from time import time 
from dotenv import load_dotenv 
import speech_recognition as sr 
import requests
#####################################################
# CONFIGURAÇÃO #####################################################

reconhecedor = sr.Recognizer()

##################################################### 
# FUNÇÃO PARA FALAR #####################################################
def speak(speechContent):
    audio =  gTTS(speechContent, lang="pt-br")
    audio.save("./bot/audios/speach.mp3")

    mixer.init()
    mixer.music.load("./bot/audios/speach.mp3")
    mixer.music.play()

    while mixer.music.get_busy():
        continue

    mixer.music.unload()

##################################################### 
# FUNÇÃO PARA TRANSCRIÇÃO DE VOZ #####################################################
def listen(): 
    with sr.Microphone() as mic: 
        print("\nAguarde...") 
        reconhecedor.adjust_for_ambient_noise(mic, duration=1) 
        print("Alexa está te ouvindo...") 
        try: 
            audio = reconhecedor.listen( mic, timeout=5, phrase_time_limit=10 ) 
        except sr.WaitTimeoutError: 
            print("Nenhuma fala detectada.") 
            return None 
        print("Reconhecendo...") 
        tempo_inicial = time() 
        try: 
            texto = reconhecedor.recognize_google( audio, language="pt-BR" ) 
            tempo_final = time() 
            print(f"Você: {texto}") 
            print( f"Tempo de reconhecimento: " f"{tempo_final - tempo_inicial:.2f}s" ) 
            return texto 
        except sr.UnknownValueError: 
            print("Não consegui entender o que você falou.") 
            return None 
        except sr.RequestError as erro: 
            print(f"Erro no serviço de reconhecimento: {erro}") 
            return None
        
##################################################### 
# LOOP PRINCIPAL #####################################################

import requests
while True:
    texto = listen()
    texto = input("Tente novamente digitando: ") if texto is None else texto
    if texto is None:
        continue
    
    # Comandos para encerrar loop
    if texto.lower() in ["sair", "exit", "quit"]:
        print("Alexa: Até mais!")
        speak("Até mais!") 
        break
    
    prompt = "Responda de forma breve e sem markdown e sem emojis:"+ texto
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "ministral-3:latest",
                "prompt": prompt,
                "stream": False
            })
        response.raise_for_status()
        resposta = response.json()["response"]
        print("Alexa:", resposta)
        speak(resposta)
        
    except requests.exceptions.ConnectionError: 
        print("Erro: não foi possível conectar ao Ollama.") 
        
    except requests.exceptions.RequestException as erro: 
        print(f"Erro na requisição: {erro}") 
    
    except Exception as erro: 
        print(f"Erro inesperado: {erro}")
#####################################################
