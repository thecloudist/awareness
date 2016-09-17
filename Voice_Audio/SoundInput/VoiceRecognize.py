
'''

Main recognition module

Uses google voice (google cloud platform) in GRPC streaming mode

Also has methods for echoing out the voice commands given after they are recognized

sound(str) speaks a string


'''


from gopigo import *
import sys
from subprocess import call
from time import sleep
from tts import *

