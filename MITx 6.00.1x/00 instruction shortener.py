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
instructions = '''

Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

Hints:
You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick a random one. Note that the functions loadWords and chooseWord should only be used on your local machine,

'''



##############################################################
debug = True
# max length of string before break.
max_len = 79
if debug:
    max_len = 20 # to make debugging easier
last_space, new_line_tracker = 0, 0

if debug: # a good starting point
    print(instructions)
    print(len(instructions), 'characters total, breaking at', max_len, '\n')
    
# use enumerate method to keep track of where we are
for position, letter in enumerate(instructions):
    if debug:
        print(position, letter, end=", ") # where are we, really?
    # take note if the character is a space
    if letter == ' ':
        last_space = position
        if debug:
            print('last_space =', last_space)
    # reset counter if there's a new line
    if letter == '\n':
        new_line_tracker = position
        if debug:
            print('New line detected, position at', position)
    # this determines if we've hit the line length
    # done as an elif because a new line is already there
    elif (position - new_line_tracker) % max_len == 0 and position != 0:
        # this replaces the last space with a newline
        instructions = instructions[:last_space] + str('\n') + \
            instructions[last_space+1:]
        # it's very ironic that this^ line goes over 80 characters
        
        if debug:
            print('newline inserted at last space. position was', position, \
                      'last space =', last_space)
            print(instructions)
        

# print the results to copy from the console
if debug:
    print('\n\nfinal:')
    print(instructions)
else:
    print(instructions)