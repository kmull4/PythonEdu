'''
We can use the idea of bisection search to determine if a character is in a
string, so long as the string is sorted in alphabetical order.

First, test
the middle character of a string against the character you're looking for (the
"test character"). If they are the same, we are done - we've found the 
character we're looking for!

If they're not the same, check if the test character is
"smaller" than the middle character. If so, we need only consider the lower 
half of
the string; otherwise, we only consider the upper half of the string. (Note
that you can compare characters using Python's < function.)

Implement the
function isIn(char, aStr) which implements the above idea recursively to test
if char
is in aStr. char will be a single character and aStr will be a string that is
in alphabetical order. The function should return a boolean value.

As you
design the function, think very carefully about what the base cases should
be.  

Note: In programming there are many ways to solve a problem. For your code to
check correctly here, though, you must write your recursive function such that
you make a recursive call directly to the function isIn. Thank you for
understanding. 
'''

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # I get how to make it recursive but I'm having trouble wrapping my head
        # around adding bisection to it as well.
    debug = False
    
    # makes a variable something to put into the recursive call
    halfway = int(len(aStr)/2)
    if debug:
        print(len(aStr), 'long', halfway, type(halfway))
    
    # is this the base case?
    if len(aStr) <= 1:
        return False
    
    # base case:
        # or maybe that's not the base case...
    if char == aStr[halfway]:
        return True
    elif char < aStr[halfway]: # lower
        aStr = aStr[:halfway]
    elif char > aStr[halfway]: # higher
        aStr = aStr[halfway:]
    else:
        print('if you see this, something went terribly wrong')
        
    
    # recursive case:
    # since it's a boolean, probably going to recurse (verb) by returning?
    return isIn(char, aStr)

# test me
print(isIn('k', 'abcdeaafkwxyzzzzz'))
