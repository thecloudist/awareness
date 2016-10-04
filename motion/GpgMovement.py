'''

The GoPiGo Movement Module
9/8/2016

'''

from gopigo import *
import sys
from subprocess import call
from time import sleep
from word2number import w2n
from positioning import Dist_Enc_Tics as d2tics
# from tts import sound
from SoundFX import *




# Text to speech in a f3 woman's voice at 150 amplitude, english, pitch = 70
def sound(spk):
	cmd_beg = "espeak -a150 -p70 -g6 -ven+f3 " # speak with 100ms pause after each phrase
	cmd_end = "' | aplay"
	print cmd_beg + spk + cmd_end
	call([cmd_beg + spk], shell=True)
# ----------------

# function to speak all three settings with a 100ms pause in between

def tell_me_what(dir,speed,distance):
	dirs='direction has been set to '+dir
	spds='speed has been set to ' + str(speed)
	dis='distance has been set to ' + str(distance)
	sound(dirs)
	sound(spds)
	sound(dis)


'''
This is the main drive method -
Takes voice enable, direction, speed and distance as argumments

on rotation turns (turns in place) multiples of 8 pertain to geometric positions
ie:  8 = 90 degrees
	16 = 180 degrees
	32 = 360 degrees

	one wheel rotates until enc_tgt is reached.
	Distance is also in encoder ticks -
	when going fwd or bwd, 18 ticks = one wheel rotation which is
'''

'''
9/20 - added dictionary-based processing - takes a dictionary sent in with commands in a specific order
No if tree to determine commands



def DriveTo(voice,dir,speed,distance):
	set_speed(speed)
	if dir == 'forward':
		if voice:
			tell_me_what(dir,speed,distance)
			fwd()
			enc_tgt(1, 1, distance)
		else:
			fwd()
			enc_tgt(1,1,distance)
	elif dir == 'back':
		if voice:
			tell_me_what(dir, speed, distance)
			bwd()
			enc_tgt(1, 1, distance)
		else:
			bwd()
			enc_tgt(1,1,distance)
	elif dir == 'left':
		if voice:
			tell_me_what(dir, speed, distance)
			left_rot()
			enc_tgt(1, 1, 8)
			while read_enc_status():
				sleep(.1)
			fwd()
			enc_tgt(1,1,distance)

		else:
			left_rot()
			enc_tgt(1, 1, 8)
			while read_enc_status():
				sleep(.1)
			fwd()
			enc_tgt(1,1,distance)
	elif dir == 'right':
		if voice:
			tell_me_what(dir, speed, distance)
			right_rot()
			enc_tgt(1, 1, 8)
			while read_enc_status():
				sleep(.1)
			fwd()
			enc_tgt(1, 1, distance)
		else:
			right_rot()
			enc_tgt(1, 1, 8)
			while read_enc_status():
				sleep(.1)
			fwd()
			enc_tgt(1, 1, distance)
	elif dir == 'stop':
		if voice:
			tell_me_what(dir, speed, distance)
			stop()
		else:
			stop()

'''
# main function - issue DriveTo commands which will say them as they are executed)

'''
Compact dictionary passed in version of DriveTo(dict)
Takes a dict with three values:
Dir, speed & distance
Future - Add bearing in degrees



def DriveToCommand(cmd_dict):
	set_speed)cmd_dict['speed']

	if cmd_dict['dir'] == 'forward':
		fwd()
		enc_tgt(1,1,cmd_dict['distance'])

'''


def DriveTo(CmdDict):
# setup variables for motion control

	PlayEffect("good")



	if CmdDict['go'] :
		dir = CmdDict['go']
	else: CmdDict['go'] = 'stop'

	if dir == 'circle':  	# to be figured out later based on diamter = distance - ie "circle 36 inches"
							# diameter = distance
		sys.exit()

	else:

		distance = d2tics(int(CmdDict['distance']))

		set_speed(int(CmdDict['speed']))
		sound("Go Forward")
		#sound(str(CmdDict["go"]+CmdDict["speed"]+CmdDict["distance"]))

		if dir == 'forward' or 'ahead':
			fwd()
			enc_tgt(1,1,distance)
		elif dir == 'backward' or 'aft':
			bwd()
			enc_tgt(1,1,distance)
		elif dir == 'left' or 'port':
			left_rot()
			enc_tgt(1, 1, 8)
			while read_enc_status():
				sleep(.1)
				fwd()
				enc_tgt(1,1,distance)

		elif dir == 'right' or 'starboard':
			right_rot()
			enc_tgt(1, 1, 8)
			while read_enc_status():
				sleep(.1)
				fwd()
				enc_tgt(1, 1, distance)
		elif dir == 'stop' or 'dock':
			stop()
		elif dir == 'circle': # to be figured out later based on diamter = distance - ie "circle 36 inches"
			# diameter = distance
			sys.exit()



# sound("Hi There")
'''
Basic control endpoints - take in some params, some none.

'''

'''




		fwd()

		left()

		right()

		bwd()

		stop()

		increase_speed()

		decrease_speed()

		print volt(),"V"

	elif a=='b': #servo test
		for i in range(180):
			servo(i)
			print i
			time.sleep(.02)


		sys.exit()

		# print us_dist(15),'cm'

		led_on(0)
		led_on(1)
		time.sleep(1)
		led_off(0)
		led_off(1)
		motor_fwd()
		motor_bwd()
		left_rot()
		right_rot()
		enc_tgt(1,1,18)
		servo(val)

		print "v",fw_ver()

		val=trim_read()
		if val==-3:
			print "-3, Trim Value Not set"
		else:
			print val-100

		print "Enter trim value to write to EEPROM(-100 to 100):",
		val=int(raw_input())
		trim_write(val)
		time.sleep(.1)
		print "Value in EEPROM: ",trim_read()-100

		print "Enter trim value to test(-100 to 100):",
		val=int(raw_input())
		trim_test(val)
		time.sleep(.1)
		print "Value in EEPROM: ",trim_read()-100


		print "Enter Servo position:",

elif a=='b': #servo test
		for i in range(180):
			servo(i)
			print i
			time.sleep(.02)

		servo(val)

	time.sleep(.1)

'''