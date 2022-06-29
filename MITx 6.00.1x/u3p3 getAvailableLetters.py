'''
Next, implement the function getAvailableLetters that takes in one parameter
- a list of letters, lettersGuessed. This function returns a string that is
comprised of lowercase English letters - all lowercase English letters that are
not in lettersGuessed.

Example Usage:

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz
Note that this function should return the letters in alphabetical order, as
in the example above.

For this function, you may assume that all the letters in lettersGuessed are
lowercase.

Hint: You might consider using string.ascii_lowercase, which is a string
comprised of all lowercase letters:

>>> import string
>>> print(string.ascii_lowercase)
abcdefghijklmnopqrstuvwxyz
'''

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    # use the hint given above
    import string
    # take a the whole lowercase ascii
    remainingLetters = string.ascii_lowercase
    # then do an if lettersGuessed in str, remove that one from the str
    for l in lettersGuessed:
        if l in remainingLetters:
            remainingLetters = remainingLetters.replace(l, '')
    # and return the final product
    return remainingLetters
