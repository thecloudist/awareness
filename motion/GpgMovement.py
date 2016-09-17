'''

The GoPiGo Movement Module
9/8/2016

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

def DriveTo(voice,dir,speed,distance):
	set_speed(speed)
	if dir == 'f':
		if voice:
			tell_me_what(dir,speed,distance)
			fwd()
			enc_tgt(1, 1, distance)
		else:
			fwd()
			enc_tgt(1,1,distance)
	elif dir == 'b':
		if voice:
			tell_me_what(dir, speed, distance)
			bwd()
			enc_tgt(1, 1, distance)
		else:
			bwd()
			enc_tgt(1,1,distance)
	elif dir == 'l':
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
	elif dir == 'r':
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

# main function - issue DriveTo commands which will say them as they are executed)





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