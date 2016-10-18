from gtts import gTTS
import os

tts = gTTS(text='Helm  Command Acknowledged', lang='en-us')
tts.save("helm_ack.mp3")

tts = gTTS(text='Helm  Acknowleged  New Course Now Set', lang='en-us')
tts.save("helm_ack_new_course.mp3")

tts = gTTS(text='Helm  Acknowleged  Full Stop', lang='en-us')
tts.save("helm_ack_full_stop.mp3")

tts = gTTS(text='Helm  Acknowledged Turning to Port', lang='en-us')
tts.save("helm_ack_turn_port.mp3")

tts = gTTS(text='Helm  Acknowledged  Warp Speed Set', lang='en-us')
tts.save("helm_ack_warp_set.mp3")

tts = gTTS(text='Helm  Acknowledged Returning to Base', lang='en-us')
tts.save("helm_ack_returning_to_base.mp3")

os.system("mpg321 helm_ack.mp3")
os.system("mpg321 helm_ack_new_course.mp3")
os.system("mpg321 helm_ack_full_stop.mp3")
os.system("mpg321 helm_ack_turn_port.mp3")
os.system("mpg321 helm_ack_warp_set.mp3")
os.system("mpg321 helm_ack_returning_to_base.mp3")
