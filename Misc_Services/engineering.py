'''
Emgineering status reports
'''

from gopigo import *

def EngStatus(stat_service):
	if stat_service == "power":
		print "Power levels sustainable at ---> " ,volt(), "megavolts\n"
	elif stat_service == "temperature":
		print "the antimatter core is very hot - like in the mega-joule range captain\n"
