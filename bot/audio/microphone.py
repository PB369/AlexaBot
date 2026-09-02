import speech_recognition as sr
from time import time
from audio.speaker import Speaker

class Microphone:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.enabled = False

    def check(self):
        # Verifica se existe um microfone disponível.
        try:
            microfones = sr.Microphone.list_microphone_names()
            if len(microfones) == 0:
                return False
            with sr.Microphone():
                pass
            self.enabled = True
            return True

        except Exception as erro:
            print(f"Microfone indisponível: {erro}")
            self.enabled = False
            return False

    def listen(self):
        if not self.enabled:
            return None
        try:
            with sr.Microphone() as mic:
                print("\nAguarde...")
                self.recognizer.adjust_for_ambient_noise(mic, duration=1)
                print("Fale algo...")

                audio = self.recognizer.listen(
                    mic,
                    timeout=5,
                    phrase_time_limit=10
                )

            print("Reconhecendo...")
            tempo_inicial = time()
            texto = self.recognizer.recognize_google(audio, language="pt-BR")
            tempo_final = time()

            print(f"Você: {texto}")
            print(f"Tempo de reconhecimento: {tempo_final - tempo_inicial:.2f}s")

            return texto

        except sr.WaitTimeoutError:
            print("Nenhuma fala detectada.")
            return None

        except sr.UnknownValueError:
            print("Fala irreconhecível.")
            return None

        except sr.RequestError as erro:
            print(f"Erro no reconhecimento de voz: {erro}")
            self.enabled = False
            return None

        except Exception as erro:
            print(f"Microfone indisponível: {erro}")
            self.enabled = False
            return None