'''
Emgineering status reports
'''

from gopigo import *

def EngStatus(stat_service):
	if stat_service == "power":
		pwrstring = str(volt())
		powerlevels = "Power Levels Sustainable At "
		return(powerlevels+pwrstring)
		# print "Power levels sustainable at ---> " ,volt(), "megavolts\n"
	elif stat_service == "temperature":
		print "the antimatter core is very hot - like in the mega-joule range captain\n"
