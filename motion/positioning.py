'''

Positioning.py - Calculate and return rotational data corresponding to encoder ticks on the wheels
Dist_Enc_Tics(inches) returns encoder tics as a function of 18 tics per rotation

eg: 'forward 10 inches' would yield - (65mm * Pi = 200mm = 8.0 inches)/18 = 23 ticks
2.25 ticks per inch.

Future feature - specify distance in any standard

ie: call feet to inches, meters to inches, millimeters to inches

'''

# wheel diameter is 65 mm :  Circumference is (Pi* 65mm = 200mm or 8 inches or 25 mm per inch)
# One Wheel Rotation = 18.0

Ticks_Per_Inch = 18.0/8.0

def Dist_Enc_Tics(inches):
    return int(round(Ticks_Per_Inch * inches,2))

'''
inches = 24n
print "Ticks per inch = %.2f " %Ticks_Per_Inch
print "Inches to move %d" %inches



print "Number of tics for %d inches = " %inches, (Dist_Enc_Tics(inches))

'''


