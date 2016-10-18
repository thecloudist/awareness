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
from positioning import *

from word2number import w2n
from positioning import Dist_Enc_Tics as d2tics

# from raspi_trek_lexicon import *
# need to use impulse under 100 and warp 100-250
# for now warp 10-100 , 1-5


def ResolveSpeed(warp_speed):
		if warp_speed == 'warpfactorone':
			return(10)

		elif warp_speed == 'warpfactortwo':
			return(30)

		elif warp_speed == 'warpfactorthree':
			return(50)

		elif warp_speed == 'warpfactorfour':
			return(75)

		elif warp_speed == 'warpfactorfive':
			return(100)

def GoAhead(speed):
	set_speed(speed)
	fwd()

def TurnToPort(degrees):
	set_speed(40)
	right_rot()
	enc_tgt(1,1,Degrees_Enc_Tics(degrees)) # turn by degrees
	# sleep(2)
	# set_speed(speed)
	# fwd()

def TurnToStarboard(degrees):
	set_speed(40)
	left_rot()
	enc_tgt(1, 1, Degrees_Enc_Tics(degrees))  # turn by degrees


def GoBackward(speed):
	set_speed(speed)
	bwd()

def AllStop(): # slow down before stopping abruptly
	set_speed(30)
	sleep(1)
	stop()

def ReturnToBase():
	sleep(1)
	stop()
	set_speed(100)
	left_rot()
	degrees = 180
	enc_tgt(1, 1, Degrees_Enc_Tics(degrees))  # turn by degrees
	sys.exit()

'''

	announcement("Returning to base")
	DriveUntilObstructed()
	Announcement("Arrived at base")
	sys.exit()

'''