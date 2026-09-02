from gtts import gTTS
from pygame import mixer
from pathlib import Path

class Speaker:
    def __init__(self):
        self.enabled = False

        raiz_bot = Path(__file__).resolve().parent.parent

        self.pasta_audio = raiz_bot / "botAudios"

        self.pasta_audio.mkdir(
            parents=True,
            exist_ok=True
        )

        self.arquivo_audio = self.pasta_audio / "speech.mp3"

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
            audio.save(self.arquivo_audio)
            if not mixer.get_init():
                mixer.init()
            mixer.music.load(self.arquivo_audio)
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