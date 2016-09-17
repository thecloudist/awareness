from gopigo import *
import sys


print "This is a basic example for the GoPiGo Robot control"
print "Press:\n\tw: Move GoPiGo Robot forward\n\ta: Turn GoPiGo Robot left\n\td: Turn GoPiGo Robot right\n\ts: Move GoPiGo Robot backward\n\tt: Increase speed\n\tg: Decrease speed\n\tx: Stop GoPiGo Robot\n\tz: Exit\n"
while True:
	print "Enter the Command:",
	a=raw_input()	# Fetch the input from the terminal
	if a=='w':
		fwd()	# Move forward
	elif a=='a':
		left()	# Turn left
	elif a=='d':
		right()	# Turn Right
	elif a=='s':
		bwd()	# Move back
	elif a=='x':
		stop()	# Stop
	elif a=='t':
		increase_speed()	# Increase speed
	elif a=='g':
		decrease_speed()	# Decrease speed
	elif a=='z':
		print "Exiting"		# Exit
		sys.exit()
	else:
		print "Wrong Command, Please Enter Again"
	time.sleep(.1)