#Use uma venv de versão 3.11 para compatibilidade com PyAudio e Speech Recognition.
#Execute comando .\.venv\Scripts\Activate.ps1 no terminal pra ativar a venv e instale as bibliotecas.

import speech_recognition as sr
from time import time

reconhecedor = sr.Recognizer()

with sr.Microphone() as mic:
    print('Aguarde')
    reconhecedor.adjust_for_ambient_noise(mic, duration=2)
    print('Fale algo')
    audio = reconhecedor.listen(mic, timeout=3, phrase_time_limit=5)
    print('Reconhecendo')
    tempo_inicial = time()
    texto = reconhecedor.recognize_google(audio, language="pt-BR")
    tempo_final = time()
    print(f"Você falou: {texto}")
    print(f"Tempo total da equisição: {tempo_final - tempo_inicial}")

    if "calcular" in texto.lower():
        lista = texto.split()
        print(lista)
        try:
            if lista[2] == "+":
                total = float(lista[1]) + float(lista[-1])
                print(f"O resultado é {total}")
            elif lista[2] == "-":
                total = float(lista[1]) - float(lista[-1])
                print(f"O resultado é {total}")
            elif lista[2] == "x":
                total = float(lista[1]) * float(lista[-1])
                print(f"O resultado é {total}")
            elif lista[2] == "/":
                if float(lista[-1]) != 0:
                    total = float(lista[1]) / float(lista[-1])
                    print(f"O resultado é {total}.")
                else:
                    print("Não é possível dividir algo por zero.")
        except IndexError:
            print("Ops, não ouvi toda sua fala")
        except Exception as erro:
            print(erro)