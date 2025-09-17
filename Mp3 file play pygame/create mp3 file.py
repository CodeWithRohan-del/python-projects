from gtts import gTTS

text = "my name is Rohan Subscribe"

tts = gTTS(text=text,lang="en")
tts.save("output.mp3")