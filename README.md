# awareness
Robotics Experimentation Project - Based on Raspberry PI 3 and GoPiGo robotic car


Setup simple motion control methods to:

Move the car in a direction at speed and distance
Also have the option of specifying voice acknowledgement of motion commands

GpgMovement is a module with motion control and voice acknowledgement.

gopigo_exerciser.py is a Simple commandline app that takes dir,speed,distance in a loop.

in Voice_Audio there are two modules:

Hear.py - Google voice recognition as a part of GCP beta service
speak.py - uses 'espeak' for text-to-speech - crude but effective.

Once the usb mini-spkr and usb mic are in, will attach that to the car so it will
be an unteathered voice-controlled car.