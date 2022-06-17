'''
Problem: copying Python instructions for these assignments doesn't fit into
the general 80 character limit.

Solution: more Python!

TO DO:
    ✔ Go back a few words and break on a space to keep words whole
    - Reset count on normal new line breaks

Idea for v2: interact with clipboard or other .py files
'''
##############################################################

# I'm thinking it's easiest to have the big string field here
instructions = '''

The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.

'''


##############################################################
debug = False
# max length of string before break. 
max_len = 79
# I wonder if I even need enumerate if this tracker is used
new_line_tracker, last_space = 0, 0

if debug:
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
            print('str:', instructions, '\n')
    # reset counter if there's a new line anyways
    # will code this later
    
    # this determines when we've hit the line length
    if (position + new_line_tracker) % max_len == 0 and position != 0:
        # this puts in a new line at the last space
        instructions = instructions[:last_space] + str('\n') + \
            instructions[last_space+1:]
        # it's very ironic that this goes over 80 characters
        if debug:
            print('insert triggered:', instructions, '\n')
        
        new_line_tracker = position - last_space
        if debug:
            print('new line tracker =', new_line_tracker)

# print the results to copy from the console
if debug:
    print('\n\nfinal:\n', instructions)
else:
    print(instructions)