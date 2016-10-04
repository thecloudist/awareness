from gtts import gTTS
import os
tts = gTTS(text='Ahhhhh      Ohhhhhh       Ahhhhh      Ehhhhhh     ooooooo', lang='en-us')
tts.save("navigatebr.mp3")
os.system("mpg321 navigatebr.mp3")
