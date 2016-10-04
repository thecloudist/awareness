from gopigo import *
import time
import random

min_distance = 70
set_speed(50)


def autonomy():
	no_problem = True
	while no_problem:
		servo(70)
		time.sleep(1)
		dist = us_dist(15)
		if dist > min_distance:
			print('Forward is fine with me', dist)
			fwd()
			time.sleep(1)
		else:
			print('Stuff is in the way', dist)
			stop()
			servo(28)
			time.sleep(1)
			left_dir = us_dist(15)
			time.sleep(1)
			servo(112)
			right_dir = us_dist(15)
			time.sleep(1)

			if left_dir > right_dir and left_dir > min_distance:
				print('Choose left!')
				left()
				time.sleep(1)
			elif left_dir < right_dir and right_dir > min_distance:
				print('Choose Right!')
				right()
				time.sleep(1)
			else:
				print('No good option, REVERSE!')
				bwd()
				time.sleep(2)
				rot_choices = [right_rot, left_rot]
				rotation = rot_choices[random.randrange(0, 2)]
				rotation()
				time.sleep(1)

			stop()


stop()
enable_servo()
servo(70)
time.sleep(3)
autonomy()
