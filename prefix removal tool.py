#!/usr/bin/env python
'''
8/1/22
This tool removes filename prefixes that are used for organization.

Also some practice adding docstrings.
'''
__author__    = "Kyle Mullen"

def main():
    import os
    
    # change these variables as needed to use this program
    directory = os.getcwd()
    filename_start = 'SpongeBob SquarePants'    # substring in the filename
    
    def remove_prefix(old_name):
        '''
        Parameters
        old_name : string
        
        Returns an edited string.
        '''
        x = old_name.find(filename_start)
        return old_name[x:] # returns the remainder of the string
    
    # name lists
    old_names = os.listdir(directory)
    new_names = []
    num_changed = 0
    
    # go through old names to determine which are relevant
    for i in old_names[:]: # must use a copy of old_names as .remove moves i
        if filename_start in i[1:]: # index 1 ignores files with no prefix
            new_names.append(remove_prefix(i))
        else:
            old_names.remove(i)
    
    # make sure old_names and new_names match up
    if len(old_names) != len(new_names):
        raise ValueError('Something has gone wrong with the lists.')
    # change the names
    for i in range(len(new_names)):
        os.rename(old_names[i], new_names[i])
        num_changed += 1
    
    # inform the user
    print(num_changed, 'file(s) changed. Press any key to exit.')
    pause = input('') # pause to let the user see what happened

if __name__ == '__main__':
    main()
