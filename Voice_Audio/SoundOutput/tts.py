'''
The main tts module

Has tell_me_what settings dir,speed,distance

Also has sound(phrase_string)

'''

from gopigo import *
import sys
from subprocess import call
from time import sleep



# Text to speech in a f3 woman's voice at 150 amplitude, english, pitch = 70
def sound(spk):
	cmd_beg = "espeak -a150 -p70 -g6 -ven+f3 --stdout '" # speak with 100ms pause after each phrase
	cmd_end = "' | aplay"
	print cmd_beg + spk + cmd_end
	call([cmd_beg + spk + cmd_end], shell=True)


# function to speak all three motion command parameters

def tell_me_what(dir,speed,distance):
	dirs='direction has been set to '+dir
	spds='speed has been set to ' + str(speed)
	dis='distance has been set to ' + str(distance)
	sound(dirs)
	sound(spds)
	sound(dis)

