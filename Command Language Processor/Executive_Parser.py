'''

Main Awareness Command Parser

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

'''
ExecParser - takes the dict 'CmdString' which was 'dictified' from voice to text by someone (google maybe?)
Parser finds out what CmdString['directive'] is and switches on that.
The switch goes to sub-parsers which are designed just to process cmd strings for that directive

Eg:  if CmdString['directive'] == "helm":
		ParseHelmCmds(CmdString)

That method skips the directive and now starts looking at subcommand key:values for helm commands

Eg: ParseHelmCmds(CmdString) -


CmdString = {'directive':directive,

actual_speed = {'warp factor 1': 30, 'warp factor 2':60, 'warp factor 3':100}

direction = CmdString[0]
Speed = CmdString[1]
actual_speed =
'warp factor 1' = 30
'warp factor 2' = 60
'warp factor 3' = 100



'''

# converts a string to a dictionary with all the junk pulled out


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

# =======

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
The executive parser which looks at directives and sends them to respective crew member routines

'''


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


'''
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
	print WarpSpeed

	if direction == 'ahead':
		GoAhead(WarpSpeed)

	elif direction == 'port': # speed will actually be degrees of turn
		TurnToPort(int(CmdString['speed']))
		print 'TurnToPort degrees -->', int(CmdString['speed'])

	elif direction == 'starboard':
		TurnToStarboard(int(CmdString['speed']))

	elif direction == 'astern':
		GoBackWard(WarpSpeed)

	elif direction == 'speed':
		WarpSpeed = ResolveSpeed(CmdString['speed'])
		set_speed(WarpSpeed)

	elif direction == 'allstop':
		ReturnToBase()

'''
Engineering
stuff like  "status power"
'''

def ParseEngCmds(EngCmdStr):
	engCmd = EngCmdStr['request']
	if engCmd == 'status':
		EngStatus(EngCmdStr['item'])


def main():

	CmdStr1 = "helm ahead warpfactor3"
	CmdStr2 = "helm speed warpfactor5"
	CmdStr3 = "helm port 45"
	CmdStr4 = "helm ahead warpfactor3"
	CmdStr5 = "helm allstop warpfactor1"
	#CmdStr5 = "Engineering status power"
	CmdStr6 = "Engineering status temperature"



# add the strings to a list of strings to run
	CmdList = [CmdStr1,CmdStr2,CmdStr3,CmdStr4,CmdStr5] #,CmdStr5,CmdStr6]

	for i in CmdList:
		CmdString = i

		CmdString = CmdString.split(' ')
		CmdString = filter(None, CmdString)

		Directive = CmdString[0]  # get the directive and test for which crew member

		CmdString.pop(0) # kick the directive off of the list so we can now convert it to a dict
		cmd = CmdString

		HelmCmdStr = {'direction': cmd[0], 'speed': cmd[1]}
		EngCmdStr = {'request': cmd[0], 'item': cmd[1]}
		CompCmdStr = {'request': cmd[0], 'item': cmd[1]}
		TactCmdStr = {'request': cmd[0], 'item': cmd[1]}
		OpsCmdStr = {'request': cmd[0], 'item': cmd[1]}
		ExecCmdStr = {'request': cmd[0], 'item': cmd[1]}

		# CmdStr = dict(zip(*[iter(CmdString)] * 2)) # convert to dict so parsers can handle it
		print "Here is the dict -->" ,cmd


		if Directive == "helm":
			HelmCmdStr['direction'] = cmd[0]
			HelmCmdStr['speed'] = cmd[1]
			print HelmCmdStr
			ParseHelmCmds(HelmCmdStr)

		elif Directive == "Computer":
			ParseComputerCmds(CmdStr)

		elif Directive == "Tactical":
			ParseTacticalCmds(CmdStr)

		elif Directive == "Engineering":
			EngCmdStr['request'] = cmd[0]
			EngCmdStr['item'] = cmd[1]
			print EngCmdStr
			ParseEngCmds(EngCmdStr)

		elif Directive == "Executive":
			ParseExecutiveCmds(CmdStr)

		elif Directive == "Ops":
			ParseOpsCmds(CmdStr)

		elif Directive == "return to base":
			ReturnToBase()
		sleep(5)







if __name__ == "__main__":
    main()
