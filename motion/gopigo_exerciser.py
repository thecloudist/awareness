from GpgMovement import DriveTo as dto
import time


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
	distance = int(raw_input("Input Distance --> "))

	time.sleep(1)


	dto(voice,dir,speed,distance)