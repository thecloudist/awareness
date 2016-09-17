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



SoundFxPath = "/home/pi/gopigo/Projects/Awareness/Voice_Audio/SoundOutput/SoundFiles/"

Good = SoundFxPath+GoodBeep
Bad = SoundFxPath+BadBeep

def PlayEffect(effect):
    if effect == 'good':
        call(["aplay", Good])
        return(True)
    elif effect == 'bad':
        call(["aplay", Bad])
        return(True)
    else:
        if effect != 'good' & effect != 'bad':
            return(False)







