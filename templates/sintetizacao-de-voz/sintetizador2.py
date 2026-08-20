from gtts import gTTS
from pygame import mixer

audio =  gTTS("Olá, mundo!", lang="pt-br")
audio.save("mundo.mp3")

mixer.init()
mixer.music.load("mundo.mp3")
mixer.music.play()

while mixer.music.get_busy():
    continue

mixer.music.unload()
