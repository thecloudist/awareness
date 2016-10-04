'''
Simulation of a Compass

With car in center circle:

	Facing North : Ping forward = Distance North
	Turn 90 Left : Ping forward = Distance West
	Turn 90 Left : Ping forward = Distance South
	Turn 90 Left : Ping forward = Distance East
	Turn 90 Left : Back to home

Every turn is remembered
90 degrees only for now
Direction is updated on the fly

To find home we need to know which way we are facing first:
We get current position of that direction by pinging ahead and back
	Ping ahead, rotate 180 and ping back
	Result is now our position along that line
	To derive distance from center, subtract current from center
	 convert difference to encoder tics and DriveTo()
Then we need to recall the length of that and the opposite direction

'''