# Navigation Services

## MapSpace() Using UltraSound Pinger 

Calculates size of space as a box
Finds the center of the box by:

Ndist + Sdist + Carlen = Height
Wdist + Edist + Carlen = Width
Center(y,x) = Height / 2, Width / 2
 

Corrects for length of car since the US sensors are on the front
Center of box is 

Find Set car facing north.
Then perform the following operations in sequence:

    Ping North
    Record distance
    Rotate 180
    Ping South
    Record distance
    
    Rotate 90 degrees right
    Ping West
    Record distance 
    Rotate 180 degrees right
    Ping East
    Record distance
    
    Normalize for length of car
    
    
    Return x,y size of space
  
## MapSpace(directional) Using Digital 3-Axis Compass


    
## GetCurrentPosition()

Finds current position by historical moves 

## Home()

Drives car to the home position based on current position.
    
    
    