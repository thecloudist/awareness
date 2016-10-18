
'''

Main recognition module

Uses google voice (google cloud platform) in GRPC streaming mode

Also has methods for echoing out the voice commands given after they are recognized

sound(str) speaks a string


'''

from GpgMovement import *
from gopigo import *
from transcribe_streaming_thread import *
from tts import *

voice = False
speed = 100
inches = 24

# this takes a list, converts to a string, strips out all non-alpha and returns it

def Textify(commands):
    commands = str(commands)
    pat = re.compile('\W')
    commands = re.sub(pat, '', commands)
    texted_cmds = commands
    print texted_cmds
    return(texted_cmds)


def main():

    stop_audio = threading.Event()
    with cloud_speech.beta_create_Speech_stub(
            make_channel('speech.googleapis.com', 443)) as service:
        try:
            listen_transcribe_loop(service.StreamingRecognize(request_stream(stop_audio), DEADLINE_SECS))
            # print "CmdSet in main -->", CmdSet
            # DriveTo(CmdSet)



        finally:
            # Stop the request stream once we're done with the loop - otherwise
            # it'll keep going in the thread that the grpc lib makes for it..
            stop_audio.set()




if __name__ == '__main__':
    main()

