# Command Language Processor

### This will process transcription strings and covert them into commands

### Requirements

* Rev 1.0 - Fixed format motion control command set
* (Future) Rev 2.0 - Variable format motion control command set, 

### Algorithm 1.0 - Motion command strings

Pass a set of commands right from recognizer to ExtractTranscript()
This calls textify() and returns a cleaned up string with spaces separating the commands
Then this string is passed to CmdStrToDict() which splits the string into a list with command pairs
Then this list is dict and zipped into a proper dictionary which is passed on to DriveTo now handling commands as key:value pairs

### Algprithm 1.1  Arbitrary commands and strings

Transcripts go into a queue. Legal command pairs {'key': val} 

## Lexicon - Commands and their alpha or numeric definitions

   * Direction Language

    ```
    Direction = 'ahead' or 'forward' = fwd | 'backward' or 'aft' = bwd | 'left' or 'port' = left |'right' or 'starboard' 
    = right| 'stop' or 'dock' = stop | 'circle' = circle
    ```

   * Course Bearing
   
   ```
   Add 'Course bearing' in 'degrees' which will need to be calculated someplace
   eg: "Course bearing mark 270 degrees"
   ```

   * Speed Language

    ```
    Speed = 'one third' = 30, 'one half' = 60, 'full' = 125, 'warp1' = 150, 'warp2' = 175, 'warp5' = 200, 'warp8' = 225, 'warp10' =250
    ```

   * Distance - Specified either in feet or inches for now
    
    ```
    Distance in feet | inches 
    ```

Each string will be converted to a value 

Returns a dictionary with the fixed format key:value

* Called with a string - ie: CmdString["ahead one-third 24 inches"] 
  * Returns a dictionary - CmdDictionary{dir:val,speed:val,distance:val}

   ```
   CmdDictionary = { direction: str('single letter'),  speed: int(speed), distance: int(distance) }
   return CmdDictionary
   Which can then be passed to DriveTo(cmd_dictionary)
   ```



