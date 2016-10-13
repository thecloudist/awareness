'''

The lexicon consists of keys and parameter values for each of the main directives

In a cmdstring :

"helm ahead warp factor 3"

helm switches to the ParseHelmCmds() method
 Then it parses the following two keys: 'direction', 'speed' and compares what was in the CmdString positions 2, 3
 The parser gets the string and uses it to index their respective dictionaries ie: direction = {'ahead':f
'''

Direction = {'ahead':GoAhead(), 'port':TurnToPort(), 'starboard':TurnToStarboard(), 'astern': GoBackward() , 'all stop': AllStop()}
Speed = {'Warp Factor 1':10, 'Warp Factor 2': 30, 'Warp Factor 3':50,'Warp Factor 4':75,'Warp Factor 5':100}