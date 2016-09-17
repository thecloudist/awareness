'''

Sound fx for aplaying out
GoodBeep
BadBeep

'''

from subprocess import call

import sys
import time

GoodBeep = ["068e.wav"]
BadBeep = ["c005.wav"]

SoundFxPath = "~/gopigo/Projects/Awareness/Voice_Audio/SoundOutput/SoundFiles/"


call(["aplay", SoundFxPath+Goodbeep])
time.sleep(1.0)
call(["aplay", SoundFxPath+BadBeep])





