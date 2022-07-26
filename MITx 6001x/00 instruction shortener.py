'''
Problem: copying Python instructions for these assignments doesn't fit into
the general 80 character limit.

Solution: more Python!

TO DO:
    ✔ Go back a few words and break on a space to keep words whole
    ✔ Reset count on normal new line breaks

Idea for v2: interact with other .py files
'''

##############################################################
# I'm thinking it's easiest to have the big string field here
instructions = '''
In this problem, you'll be asked to read through an object-oriented implementation of the hand from the word game problem of Problem Set 4. You'll then be asked to implement one of its methods. Note that the implementation of the object-oriented version of the hand is a bit different than how we did things with the functional implementation; pay close attention to doc strings and read through the implementation carefully.

To begin: Download hand.py and read through the file. Be sure to understand what's going on in the file. Make a few instances of the Hand class, and play around with the existing methods.

When you have completed reading through the file, implement the update method.

Paste the entire Hand class in the box below.
'''



##############################################################
# variables that need initializing
last_space, new_line_tracker, max_len = 0, 0, 78
debug = False
# example to keep that actually broke something
if debug == True:
    max_len = 20 # to make debugging easier
    instructions = '''Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!

Example Usage:
When inserting underscores into your string, it's a good idea to add at least a space after each one, so it's clear to the user how many unguessed letters are left in the string (compare the readability of ____ with _ _ _ _ ). This is called usability - it's very important, when programming, to consider the usability of your program. If users find your program difficult to understand or operate, they won't use it!

For this problem, you are free to use spacing in any way you wish - our grader will only check that the letters and underscores are in the proper order; it will not look at spacing. We do encourage you to think about usability when designing.
For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.'''

# functions~
def append_log(mystr):
    # log text file. easier to read than console output.
    # takes in a string, adds string to the log
    mystr = str(mystr)
    f.write(mystr)
    return

def is_new_line_needed():
    # determines if new line is needed or not
    if position == 0 or new_line_tracker == 0:
        return False
    elif new_line_tracker % max_len == 0:
        return True
    else:
        return False

def new_line_inserter():
    global instructions, new_line_tracker
    instructions = instructions[:last_space] + str('\n') + \
        instructions[last_space+1:]
        # it's rather ironic that this^ line goes over 80 characters
    new_line_tracker = position - last_space
    return

# clear previous log
f = open('01_log.txt', "w") # this saves in \users\me by default
f.write("")
f.close()
# now write a new one
f = open('01_log.txt', "a")
# a good starting point to log
append_log(instructions)
append_log('\n' + str(len(instructions)) + ' characters total, ')
append_log('breaking at ' + str(max_len) + '\n~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')

# use enumerate method to keep track of where we are
for position, letter in enumerate(instructions):
    append_log(str(position) +' '+ str(letter) + \
               ', ') # where are we, really?
    # take note if the character is a space
    if letter == ' ':
        last_space = position
        append_log('\nlast_space = ' + str(last_space) + '\n')
    
    # reset counters and skip new line checker if there's a new line
    if letter == '\n':
        last_space = position
        new_line_tracker = -1 # because it adds it back soon
        append_log('New line detected, position at ' + str(position) +'\n')
    # if it is a new line already, don't check for new line
    elif is_new_line_needed():
        new_line_inserter()
        append_log('newline inserted at last space. position now ' + \
                   str(position) + ', last space = ' + str(last_space) + \
                       ', new_line_tracker = ' + str(new_line_tracker))
        append_log('\n~~vv~~\n' + str(instructions) + '\n~~^^~~\n\n')
    new_line_tracker += 1

# log the final values
append_log('\n\nfinal:\n' + instructions)

# print in the console to copy and use
print(instructions)

# close the log
f.close()
