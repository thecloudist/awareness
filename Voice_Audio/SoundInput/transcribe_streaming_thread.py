#!/usr/bin/python
# Copyright (C) 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Sample that streams audio to the Google Cloud Speech API via GRPC."""

from __future__ import division

import contextlib
import Queue
import re
import threading

from google.cloud import credentials
# older approach - from gcloud.credentials import get_credentials
from google.cloud.speech.v1beta1 import cloud_speech_pb2 as cloud_speech
from google.rpc import code_pb2
from grpc.beta import implementations
import pyaudio
import json
from gopigo import *
from GpgMovement import DriveTo
from positioning import Dist_Enc_Tics as d2tics
from sys import exit

# Audio recording parameters
RATE = 44100
CHANNELS = 1
CHUNK = 512

voice = False
speed = 100
inches = 24

# Keep the request alive for this many seconds
DEADLINE_SECS = 8 * 60 * 60
SPEECH_SCOPE = 'https://www.googleapis.com/auth/cloud-platform'


def make_channel(host, port):
    """Creates an SSL channel with auth credentials from the environment."""
    # In order to make an https call, use an ssl channel with defaults
    ssl_channel = implementations.ssl_channel_credentials(None, None, None)

    # Grab application default credentials from the environment
    creds = credentials.get_credentials().create_scoped([SPEECH_SCOPE])
    # Add a plugin to inject the creds into the header
    auth_header = (
        'Authorization',
        'Bearer ' + creds.get_access_token().access_token)
    auth_plugin = implementations.metadata_call_credentials(
        lambda _, cb: cb([auth_header], None),
        name='google_creds')

    # compose the two together for both ssl and google auth
    composite_channel = implementations.composite_channel_credentials(
        ssl_channel, auth_plugin)

    return implementations.secure_channel(host, port, composite_channel)


class Readable():
    def __init__(self, q):
        self.q = q

    def read(self, *args):
        data = [self.q.get()]
        while True:
            try:
                data.append(self.q.get(block=False))
            except Queue.Empty:
                break
        return b''.join(data)

def fill_buffer(audio_stream, q, chunk, stop_audio):
    while not stop_audio.is_set():
        data = audio_stream.read(chunk)
        q.put(data)


# [START audio_stream]
@contextlib.contextmanager
def record_audio(channels, rate, chunk, stop_audio):
    """Opens a recording stream in a context manager."""
    audio_interface = pyaudio.PyAudio()
    audio_stream = audio_interface.open(
        format=pyaudio.paInt16, channels=channels, rate=rate,
        input=True, frames_per_buffer=chunk,
    )

    q = Queue.Queue()
    buff = Readable(q)
    fill_buffer_thread = threading.Thread(target=fill_buffer,
            args=(audio_stream, q, chunk, stop_audio))
    fill_buffer_thread.start()

    yield buff

    audio_stream.stop_stream()
    audio_stream.close()
    audio_interface.terminate()
# [END audio_stream]


def request_stream(stop_audio, channels=CHANNELS, rate=RATE, chunk=CHUNK):
    """Yields `StreamingRecognizeRequest`s constructed from a recording audio
    stream.

    Args:
        stop_audio: A threading.Event object stops the recording when set.
        channels: How many audio channels to record.
        rate: The sampling rate in hertz.
        chunk: Buffer audio into chunks of this size before sending to the api.
    """
    # The initial request must contain metadata about the stream, so the
    # server knows how to interpret it.
    recognition_config = cloud_speech.RecognitionConfig(
        # There are a bunch of config options you can specify. See
        # https://goo.gl/A6xv5G for the full list.
        encoding='LINEAR16',  # raw 16-bit signed LE samples
        sample_rate=rate,  # the rate in hertz
        # See
        # https://g.co/cloud/speech/docs/best-practices#language_support
        # for a list of supported languages.
        language_code='en-US',  # a BCP-47 language tag
    )
    streaming_config = cloud_speech.StreamingRecognitionConfig(
        config=recognition_config,
    )

    yield cloud_speech.StreamingRecognizeRequest(
        streaming_config=streaming_config)

    with record_audio(channels, rate, chunk, stop_audio) as audio_stream:
        while not stop_audio.is_set():
            data = audio_stream.read(chunk)
            if not data:
                raise StopIteration()

            # Subsequent requests can all just have the content
            yield cloud_speech.StreamingRecognizeRequest(audio_content=data)


def listen_transcribe_loop(recognize_stream):
    CommandSet = {}
    for resp in recognize_stream:
        if resp.error.code != code_pb2.OK:
            raise RuntimeError('Server error: ' + resp.error.message)

        # Display the transcriptions & their alternatives
        for result in resp.results:
            # convert the raw transcript into a string of words and spaces (cmdstr)
            # ???????
            cmdstr = extract_transcript(str(result.alternatives))
            # print "after extract_transcript -->",cmdstr
            # now convert the cmdstr into a CommandSet{} dictionary
            # CommandSet = CmdStrToDict(cmdstr) # returns dictionary of CommandSet
            print "From the loop -->",cmdstr
            return cmdstr

            # DriveTo(CommandSet) # pass the CommandSet dictionary to DriveTo

        # Exit recognition if any of the transcribed phrases could be
        # one of our keywords.
        if any(re.search(r'\b(exit|quit)\b', alt.transcript)
               for result in resp.results
               for alt in result.alternatives):
            print('Exiting..')
            sys.exit()

            #return 'False

'''
CmdStrToDict(cmdstr)
Converts a command string of space delimeted commands and values into a proper dictionary
Returns a dictionary

'''

def CmdStrToDict(cmdstr):
# first convert string to list
    # print "Inside CmdStrToDict before split -->", cmdstr

    cmdstr = cmdstr.split(' ')
    # print  "Inside CmdStrToDict after split cmdstr -->",cmdstr
    cmdstr = filter(None, cmdstr)
    # print  "Inside CmdStrToDict after split cmdstr -->",cmdstr
# Nice little zip thing that dict-a-fies the cmdstr with 1st = key, 2nd = value from separate commands
    cmd_dict = dict(zip(*[iter(cmdstr)]*2))
    return cmd_dict




'''
Crack out the "quoted" stuff in the response.
Uses Regex to do it, quite cute.  (Thanks to http://stackoverflow.com/users/95810/alex-martelli)
'''

def extract_transcript(transcript_result):
    # type(transcript_result)
   # print ("transcript_results --> %s" %transcript_result
    quoted = re.compile('"[^"]*"')  # quoted = re.compile('"[^"]*"')
    # print "quoted -->" , quoted
    for value in quoted.findall(transcript_result):
        # print ("Value --> %s " % value)
        pattern = Textify(value)
        # print ("pattern after textify --> %s" %pattern)
        # return a dictionary of key:values
        return pattern


# this takes a list, converts to a string, strips out all non-alpha and returns it

def Textify(commands):
    commands = str(commands)
    pat = re.compile('\W')
    commands = re.sub(pat, ' ', commands)
    texted_cmds = commands
    return(texted_cmds)

'''

Commented out - This will run in VoiceControlCar.py - 09/18/2016

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
'''