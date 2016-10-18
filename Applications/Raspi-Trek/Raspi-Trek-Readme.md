# Raspi-Trek

A project to simulate starship enterprise with the nextgen crew on a Raspberry Pi in the GoPiGo robot car.

## Premise

Using a USB mic plugged into the GoPiGo, The 'Captain' issues voice commands to the crew of the
Enterprise and they carry them out as prescribed.  

Commands are loosely based on the familiar lexicon of Star-Trek, TNG.

These commands are immediately streamed to Google Cloud Speech
and transcriptions are shot back momentarily.  

The Raspi-Trek Python main program cracks these with parsers and some formatting into clean dictionaries which are then passed to control methods to take some actions.

There are two speech output methods for announcing that come through a small, 
powered analog speaker sitting on top of the car.  

There is also a sound effects engine that play pre-recorded annunciations for specific status or command acknowledgements.

## Sensors

* Ultrasonic proximity pingers
* HD Camera
* 3-Axis Digital Compass

## Transducers

* USB Microphone 
* Analog speaker
* LEDs

## Servo

* 180 degrees of positioning for the Ultrasonic sensors

## Software

* OS - Raspbian Jessie
* Python 2.7
* Pyaudio
* Alsa
* espeak (tts) Immediate vocalization very robotic
* mpg321 MP3 audio player - takes gTTS mp3 files and plays them programmatically
* Google text to speech (gTTS) for a nicer voice, slightly robotic
* Google Cloud Speech - GRPC version PB .2 streaming, multi-threaded
* Gopigo libraries
* GPIO * SMBUS libraries for Pi

## Lexicon
Refer to raspi-trek-commands.xlsx for a complete list and hierarchy

* Helm
* Engineering
* Computer
* Tactical
* Ops
* Executive

## Architecture
Current approach is to loop on capturing audio, send off to Google Speech and dispatch on transcribed commands coming in.

There are parsers to slice up command strings and pass the remaining commands to appropriate 'crew members'

Directives at the head of any command string are the 6 'crew' member parsers.
Once the directive is found, it is popped off of the list and the remaining list is struck to a dictionary.
This is sent to the crew dispatch ie: ParseHelmCmds(cmdstr) and it is ready to be dispatched to control methods for each of the crew.

## Future 

* Guided Missions
* Location-based navigation with waypoints
* Supervised Machine-Learning 
* Video streaming 
* Bluetooth headset integration
* Image recognition via Google Cloud Vision
* Network coordination with another vehicle

## Way in the future

* Port this whole thing to a real car
* Port this to a drone quadcopter and boat



