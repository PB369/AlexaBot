from gtts import gTTS
from pygame import mixer

class Speaker:
    def __init__(self):
        self.enabled = False

    def check(self):
        try:
            if not mixer.get_init():
                mixer.init()
            self.enabled = True
            return True
        
        except Exception as erro:
            print(f"Saída de áudio indisponível: {erro}")
            self.enabled = False
            return False

    def speak(self, texto):
        if not self.enabled:
            return

        try:
            audio = gTTS(texto, lang="pt-br")
            audio.save("./botAudios/speech.mp3")
            if not mixer.get_init():
                mixer.init()
            mixer.music.load("./audios/speech.mp3")
            mixer.music.play()

            while mixer.music.get_busy():
                pass
            
            mixer.music.unload()

        except Exception as erro:
            print(f"Não foi possível reproduzir o áudio: {erro}")
            self.enabled = False
            try:
                mixer.quit()
            except:
                pass