'''
Problem: copying Python instructions for these assignments doesn't fit into
the general 80 character limit.

Solution: more Python!

TO DO:
    ✔ Go back a few words and break on a space to keep words whole
    ✔ Reset count on normal new line breaks

Idea for v2: interact with clipboard or other .py files
'''
##############################################################

# I'm thinking it's easiest to have the big string field here
instructions = '''Note: In programming there are many ways to solve a problem.
For example, some asled dsfgsdfg dfjasdfg jwfe oej fmay aljw43td f ljawo48jgf ad when a09s8df0 98098 but also owjaf23.

Understandably, 304dsfg sdfg 9 sdfg sdfg sdfssdfg dfg 8tjqg3sdfg 567df g3 scgbn saapjefg!!!!

Oh man, it's so close.
But I need to take a break and test this fork situation too.'''


##############################################################
debug = True
# max length of string before break.
max_len = 79
if debug:
    max_len = 20 # to make debugging easier
# variables for later use
new_line_tracker, last_space = 0, 0

if debug: # a good starting point
    print(instructions)
    print(len(instructions), 'characters total\n')
    
# use enumerate method to keep track of where we are
for position, letter in enumerate(instructions):
    if debug:
        print(position, letter, end=", ") # where are we, really?
    # take note if the character is a space
    if letter == ' ':
        last_space = position
        if debug:
            print('last_space =', last_space)
            #print('str:', instructions, '\n')
    # reset counter if there's a new line
    # aha, coding it now
    # I'm pretty sure that if this is triggered, skip the next part.
        # so I made it an elif
    if letter == '\n':
        new_line_tracker = position
        if debug:
            print('New line detected, _tracker now = position at', new_line_tracker)
    # this determines if we've hit the line length
    # self: position + new line because it needs to trigger x steps earlier
    elif (position + new_line_tracker) % max_len == 0 and position != 0:
        # this replaces the last space with a newline
        instructions = instructions[:last_space] + str('\n') + \
            instructions[last_space+1:]
        # it's very ironic that this^ line goes over 80 characters
        if debug:
            print('newline inserted at last space. position =', position, \
                  'new_line_tracker =', new_line_tracker, \
                      'last space =', last_space)
            print(instructions)
        # new_line_tracker needs to be offset
        new_line_tracker = last_space
        if debug:
            print('new line tracker = last_space =', \
                  new_line_tracker, '\n')

# print the results to copy from the console
if debug:
    print('\n\nfinal:')
    print(instructions)
else:
    print(instructions)