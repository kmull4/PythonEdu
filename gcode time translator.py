# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
November 2023
Gcode files exported by Cura have the time in the beginning but in seconds
This finds the time if it exists and adds the time in hours/minutes
"""

__author__    = "Kyle Mullen"


def main():
    file_name = "C:/Users/RedPC/Documents/GitHub/PythonEdu/example_gcode.gcode"  #TODO make this be a list of all the files in the folder
    
    with open(file_name, 'r+') as f:
    
        new_code = ""            # where the new modified code will be put
        content = f.readlines()  # gcode as a list where each element is a line 
        
        timeInSeconds = int(content[1][6:])
        timeInHours = round(timeInSeconds/60/60,2)
        
        secondLine = ";TIME: " + str(timeInHours) + " hours\n"
        content[1] = secondLine
        
        # build the string from the list
        new_code = ''.join(map(str, content))
        
        f.seek(0)           # set the cursor to the beginning of the file
        f.write(new_code)   # write the new code over the old one

if __name__ == '__main__':
    main()
