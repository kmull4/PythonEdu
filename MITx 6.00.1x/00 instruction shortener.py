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

Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!

Example Usage:

>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getGuessedWord(secretWord, lettersGuessed))
'_ pp_ e'
When inserting underscores into your string, it's a good idea to add at least a space after each one, so it's clear to the user how many unguessed letters are left in the string (compare the readability of ____ with _ _ _ _ ). This is called usability - it's very important, when programming, to consider the usability of your program. If users find your program difficult to understand or operate, they won't use it!

For this problem, you are free to use spacing in any way you wish - our grader will only check that the letters and underscores are in the proper order; it will not look at spacing. We do encourage you to think about usability when designing.

For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.



'''



##############################################################
debug = False

# example to keep that actually broke something
if debug == True:
    instructions = '''
    
    Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!

    Example Usage:

    >>> secretWord = 'apple' 
    >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    >>> print(getGuessedWord(secretWord, lettersGuessed))
    '_ pp_ e'
    When inserting underscores into your string, it's a good idea to add at least a space after each one, so it's clear to the user how many unguessed letters are left in the string (compare the readability of ____ with _ _ _ _ ). This is called usability - it's very important, when programming, to consider the usability of your program. If users find your program difficult to understand or operate, they won't use it!

    For this problem, you are free to use spacing in any way you wish - our grader will only check that the letters and underscores are in the proper order; it will not look at spacing. We do encourage you to think about usability when designing.

    For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.

    
    '''

# max length of string before break.
max_len = 78
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