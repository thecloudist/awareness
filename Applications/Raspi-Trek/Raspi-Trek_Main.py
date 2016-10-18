'''

	Raspi-Trek Main

	Commands can come in different lengths
	Directives lead the command strings

	Awareness for Raspi-Trek

	Directives:

	"Helm"      : Controlling the movement of the vehicle including navigation

		"Ahead", int(speed), int(distance)
		"Astern", int(speed), int(distance)
		"Port", s,d  (Left)
		"Starboard", s,d (Right)
		"Slow" int(speed) Slow down to "one third", "one half"
		"speed" int(speed) set the speed to a value
		"set course for", direction(compass heading) which would be followed by a movement command

	eg: "helm"  'ahead 30 distance 48'
		"helm"  'port 20 distance 32'
		"helm"  'starboard 60 distance 120'
		"helm"  'slow 1/3'

	"Computer"  : Asking questions of the A.I.
	"Tactical"  : Weapons, sensors and intel
	"Engineer"  : Status of ship, power, damage
	"Exec"      : Starfleet, directives, 1st officer
	"Ops"       : TBD'd


'''

from HelmsMan import *
from engineering import *
import sys
from time import sleep
from gtts import gTTS
import os
from tts import sound
from transcribe_streaming_thread import *
from SoundFX import *



audio_resp_dir = "/home/pi/Awareness/Applications/Raspi-Trek/audio_responses/"

# converts a string to a dictionary with all the junk pulled out


'''
The executive parser which looks at directives and sends them to respective crew member routines




def ExecParser(Directive):
	while Directive != "back to base":
		if Directive == "helm":
			ParseHelmCmds(CmdString)
		elif Directive == "Computer":
			ParseComputerCmds(CmdString)
		elif Directive == "Tactical":
			ParseTacticalCmds(CmdString)
		elif Directive == "Engineer":
			ParseEngineer(CmdString)
		elif Directive == "Executive":
			ParseExecutiveCmds(CmdString)
		elif Directive == "Ops":
			ParseOpsCmds(CmdString)

	ReturnToBase()



ParseHelmCmds -

Dictionary to recall tokens from spoken keys:

direction = {'adjust speed': 'warp factor x' ahead':GoAhead(), 'port':TurnToPort(), 'starboard':TurnToStarboard(), 'astern': GoBackward() , 'all stop': AllStop()}
speed = {'Warp Factor 1':10, 'Warp Factor 2': 30, 'Warp Factor 3':50,'Warp Factor 4':75,'Warp Factor 5':100}

CmdString will contain "ahead warp factor 2"
or "starboard" then "ahead warp factor 3"

'''

def ParseHelmCmds(CmdString):

	direction = CmdString['direction']
	WarpSpeed = ResolveSpeed(CmdString['speed'])
	aresp_dir = audio_resp_dir
	print WarpSpeed

	if direction == 'ahead':
		os.system("mpg321 "+aresp_dir+"helm_ack_new_course.mp3")
		GoAhead(WarpSpeed)

	elif direction == 'port': # speed will actually be degrees of turn
		TurnToPort(int(CmdString['speed']))
		os.system("mpg321 "+aresp_dir+"helm_ack_turn_port.mp3")
		print 'TurnToPort degrees -->', int(CmdString['speed'])

	elif direction == 'starboard':
		TurnToStarboard(int(CmdString['speed']))

	elif direction == 'astern':
		GoBackWard(WarpSpeed)

	elif direction == 'speed':
		os.system("mpg321 "+aresp_dir+"helm_ack_warp_set.mp3")
		WarpSpeed = ResolveSpeed(CmdString['speed'])
		set_speed(WarpSpeed)

	elif direction == 'allstop':
		os.system("mpg321 "+aresp_dir+"helm_ack_full_stop.mp3")
		ReturnToBase()

'''
Engineering
stuff like  "status power"
pull out the request and dispatch to engineering.py
'''

def ParseEngCmds(EngCmdStr):
	engCmd = EngCmdStr['request']
	if engCmd == 'status':
		sound(EngStatus(EngCmdStr['item']))




'''
Computer
stuff like  "Compute flight time until we reach examitus-4"


def ParseComputerCmds(ComputerCmdStr):
	ComputerCmd = ComputerCmdStr['request']
	if ComputerCmd == 'status':
		ComputerStatus(EngCmdStr['item'])

Engineering
stuff like  "status power"


def ParseEngCmds(EngCmdStr):
	engCmd = EngCmdStr['request']
	if engCmd == 'status':
		EngStatus(EngCmdStr['item'])

Engineering
stuff like  "status power"


def ParseEngCmds(EngCmdStr):
	engCmd = EngCmdStr['request']
	if engCmd == 'status':
		EngStatus(EngCmdStr['item'])

'''



'''
This would be where main() asks for transcripts in a loop
It would call listen_transcribe_loop() and a list instead of a dict would be returned
This list may be called CmdString or something.  The 0'th element is the 'Directive' and the next two things are commands and data
We pop the directive out of the list so we can more easily split and then convert the list to a dict.
crew routines know how to access the cmdstr params by integer indices such as list[0] or list[1]






	#  This simulates commands coming from GSpeech rec

CmdStr1 = "helm ahead warpfactor3"
	CmdStr2 = "helm speed warpfactor5"
	CmdStr3 = "helm port 45"
	CmdStr4 = "helm ahead warpfactor3"
	CmdStr6 = "helm allstop warpfactor1"
	CmdStr5 = "Engineering status power"
	#CmdStr6 = "Engineering status temperature"

# add the strings to a list of strings to run
	CmdList = [CmdStr1,CmdStr2,CmdStr3,CmdStr4,CmdStr5,CmdStr6]

for i in CmdList:
		CmdString = i

		CmdString = CmdString.split(' ')
		CmdString = filter(None, CmdString)

		Directive = CmdString[0]  # get the directive and test for which crew member

		CmdString.pop(0) # kick the directive off of the list so we can now convert it to a dict
		cmdstr = CmdString
'''
#
#
#

'''

Main function

using a 'with/try/finally loop for getting speech commands and dispatching them via the parsers
Uses a returned string 'cmdstr' which it parses out for directive, cmds and data
Then is pops the directive ie: helm, engineering etc and stuffs that into the 'Directive' var.
Then runs through the executive parser inline with directive and dispatches to a crew parser which knows what to look for in the predefined
dict that has been stuffed from the command string.

Problem:  How to get looping going on everything in main without dropping out - 10/17 - 5:31 PM

'''

def main():

	good = "good"
	bad = "bad"
	Directive = "blah"
	while Directive != "quit":
		# Invoke the threaded audio acquisition methods in t_s_t.py
		stop_audio = threading.Event()
		with cloud_speech.beta_create_Speech_stub(
				make_channel('speech.googleapis.com', 443)) as service:
			try:
				cmdstr = listen_transcribe_loop(service.StreamingRecognize(request_stream(stop_audio), DEADLINE_SECS))
				print "right after listen_transcribe_loop is called -->",cmdstr

				cmdstr = cmdstr.split(' ')
				cmdstr = filter(None, cmdstr)

				Directive = cmdstr[0]  # get the directive and test for which crew member

				cmdstr.pop(0)  # kick the directive off of the list so we can now convert it to a dict
				print "right after pop -->", cmdstr

				HelmCmdStr = {'direction': cmdstr[0], 'speed': cmdstr[1]}
				EngCmdStr = {'request': cmdstr[0], 'item': cmdstr[1]}
				CompCmdStr = {'request': cmdstr[0], 'item': cmdstr[1]}
				TactCmdStr = {'request': cmdstr[0], 'item': cmdstr[1]}
				OpsCmdStr = {'request': cmdstr[0], 'item': cmdstr[1]}
				ExecCmdStr = {'request': cmdstr[0], 'item': cmdstr[1]}

				print "Directive before execparser -->",Directive
				print "HelmCmdStr{} = ",HelmCmdStr

				if Directive == "Helm":
					PlayEffect(good)
					sleep(.5)
					HelmCmdStr['direction'] = cmdstr[0]
					print "Directive == Helm so HelmCmdStr['direction'] == --> ", HelmCmdStr['direction']
					HelmCmdStr['speed'] = cmdstr[1]+cmdstr[2]+cmdstr[3]
					print "HelmCmdStr['speed'] == ",HelmCmdStr['speed']
					ParseHelmCmds(HelmCmdStr)

				elif Directive == "Computer":
					ParseComputerCmds(CmdStr)

				elif Directive == "Tactical":
					ParseTacticalCmds(CmdStr)

				elif Directive == "Engineering":
					EngCmdStr['request'] = cmdstr[0]
					EngCmdStr['item'] = cmdstr[1]
					ParseEngCmds(EngCmdStr)

				elif Directive == "Executive":
					ParseExecutiveCmds(CmdStr)

				elif Directive == "Ops":
					ParseOpsCmds(CmdStr)

				elif Directive == "return to base":
					ReturnToBase()
				sleep(5)


			finally:
				# Stop the request stream once we're done with the loop - otherwise
				# it'll keep going in the thread that the grpc lib makes for it..
				stop_audio.set()










if __name__ == "__main__":
    main()
