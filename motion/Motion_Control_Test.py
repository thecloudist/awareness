from gopigo import *
from positioning import Dist_Enc_Tics as d2tics
from GpgMovement import *
from time import sleep

print volt()
time.sleep(1)


while dir != 'x':

	print "dir = f,b,l,r\n"
	print "speed = 0-255\n"
	print "distance = multiples or fractions of 18 = 1 rotation"

	v = raw_input("Do you want voice output on this run? (y/n) --> ")
	if v == 'y':
		voice = True
	else: voice = False
	dir = raw_input("Input Direction --> ")
	if dir == 'x':
		break
	speed = int(raw_input("input Speed --> "))
	inches = int(raw_input("Input Distance in inches --> "))

	sleep(1)


	DriveTo(voice,dir,speed,d2tics(inches))



