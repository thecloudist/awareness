'''

Sound fx for aplaying out
GoodBeep
BadBeep

Right

'''

from subprocess import call

import sys
import time

GoodBeep = "voc22.wav"
BadBeep = "c005.wav"

Aplay_Cmd_Params = " -D hw:0,0 -c1 -f cd "

SoundFxPath = "/home/pi/gopigo/Projects/Awareness/Voice_Audio/SoundOutput/SoundFiles/"

GoodSound = Aplay_Cmd_Params+SoundFxPath+GoodBeep
BadSound = Aplay_Cmd_Params+SoundFxPath+BadBeep
AplayCmd = "aplay"

def PlayEffect(effect):
    if effect == 'good':
        print GoodSound
        call([AplayCmd + GoodSound],shell=True)
        return(True)
    elif effect == 'bad':
        print BadSound
        call([AplayCmd + BadSound],shell=True)
        return(True)
    else:
        if effect != 'good' & effect != 'bad':
            return(False)







