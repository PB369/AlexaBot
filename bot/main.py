from gtts import gTTS
from pygame import mixer
from time import time
from groq import Groq
import os
from dotenv import load_dotenv
#####################################################
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
load_dotenv()
client = Groq(
   api_key=os.getenv("GROQ_API_KEY")
)

tempo_inicial = time()

def generateResponse(userMessage):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "Você é um assistente útil e objetivo."
            },
            {
                "role": "user",
                "content": userMessage
            }
        ]
    )

    tempo_final = time()
    print(f"Tempo da requisição: {tempo_final - tempo_inicial}s")
    speak(response.choices[0].message.content)

#####################################################
import requests
while True:
    texto = input("Você: ")
    prompt = "Responda de forma breve e sem markdown e sem emojis:"+ texto
    if texto.lower() in ["sair", "exit", "quit"]:
        break
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "ministral-3:latest",
            "prompt": prompt,
            "stream": False
        })
    resposta = response.json()
    print("Alexa:", resposta['response'])
    speak(resposta['response'])
#####################################################
# message = input('Faça uma pergunta para a Alexa: ')
# generateResponse(message)