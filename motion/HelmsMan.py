'''

Helmsman module

Includes some motion commands like ReturnToBase()

direction = {'adjust speed': 'warp factor x' ahead':GoAhead(), 'port':TurnToPort(), 'starboard':TurnToStarboard(), 'astern': GoBackward() , 'all stop': AllStop()}
speed = {'Warp Factor 1':10, 'Warp Factor 2': 30, 'Warp Factor 3':50,'Warp Factor 4':75,'Warp Factor 5':100}

Future - Add angular coordinates such as "port 40 degrees"
No speed for turn commands for now - defaults to Warp 1

'''

from gopigo import *
import sys
from subprocess import call
from time import sleep

from word2number import w2n
from positioning import Dist_Enc_Tics as d2tics
# from raspi_trek_lexicon import *


def ResolveSpeed(warp_speed):
		if warp_speed == 'warpfactor1':
			return(10)

		elif warp_speed == 'warpfactor2':
			return(30)

		elif warp_speed == 'warpfactor3':
			return(50)

		elif warp_speed == 'warpfactor4':
			return(75)

		elif warp_speed == 'warpfactor5':
			return(100)

def GoAhead(speed):
	set_speed(speed)
	fwd()

def TurnToPort(speed):
	set_speed(40)
	right_rot()
	enc_tgt(1,1,8) # just 90 degrees for now
	sleep(2)
	set_speed(speed)
	fwd()

def TurnToStarboard():
	left_rot()
	enc_tgt(1, 1, 8)  # just 90 degrees for now

def GoBackward(speed):
	set_speed(speed)
	bwd()

def AllStop(): # slow down before stopping abruptly
	set_speed(30)
	stop()

def ReturnToBase():
	stop()
	rotate(180)
	sys.exit()

'''

	announcement("Returning to base")
	DriveUntilObstructed()
	Announcement("Arrived at base")
	sys.exit()

'''