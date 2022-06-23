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

<<<<<<< Updated upstream
Understandably, 304dsfg sdfg 9 sdfg sdfg sdfssdfg dfg 8tjqg3sdfg 567df g3 scgbn saapjefg!!!!

Oh man, it's so close.
But I need to take a break and test this fork situation too.'''
=======
You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)

Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

'''
>>>>>>> Stashed changes


##############################################################
debug = True
<<<<<<< Updated upstream
# max length of string before break.
max_len = 79
if debug:
    max_len = 20 # to make debugging easier
# variables for later use
=======
# max length of string before break. 
max_len = 78
# I wonder if I even need enumerate if this tracker is used
>>>>>>> Stashed changes
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