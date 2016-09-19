
'''

Main recognition module

Uses google voice (google cloud platform) in GRPC streaming mode

Also has methods for echoing out the voice commands given after they are recognized

sound(str) speaks a string


'''


# from gopigo import *
import sys
from subprocess import call
from time import sleep
# from tts import *

from transcribe_streaming_thread import *

def main():
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


if __name__ == '__main__':
    main()

