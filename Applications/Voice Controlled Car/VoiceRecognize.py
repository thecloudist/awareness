
'''

Main recognition module

Uses google voice (google cloud platform) in GRPC streaming mode

Also has methods for echoing out the voice commands given after they are recognized

sound(str) speaks a string


'''


from gopigo import *
from GpgMovement import *
import sys
from subprocess import call
from time import sleep
from tts import *
from positioning import Dist_Enc_Tics as d2tics
from transcribe_streaming_thread import *
from time import sleep



def recog_loop():
    stop_audio = threading.Event()
    with cloud_speech.beta_create_Speech_stub(
            make_channel('speech.googleapis.com', 443)) as service:
        try:
            listen_print_loop(
                service.StreamingRecognize(
                    request_stream(stop_audio), DEADLINE_SECS))
        finally:
            # Stop the request stream once we're done with the loop - otherwise
            # it'll keep going in the thread that the grpc lib makes for it..
            stop_audio.set()

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

# if __name__ == '__main__':
#    main()

