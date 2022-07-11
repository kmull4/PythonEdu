'''

Instructons here

'''
def isWordGuessed(secretWord, lettersGuessed):
    '''
secretWord: string, the word the user is guessing
lettersGuessed: list, what letters have been guessed so far

returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for l in secretWord:
        if l not in lettersGuessed:
            return False
    # once the for loop is completed
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    debug = False
    index = 0
    for l in secretWord:
        if debug:
            print('l =', l, 'index =', index)
        # if not in lettersGuessed, make an underscore
        if l not in lettersGuessed:
            secretWord = secretWord[:index] + str('_ ') + secretWord[index+1:]
            if debug:
                print('l not in lettersGuessed, secretWord now =', secretWord)
            index += 1 # this was the missing key
        index += 1
        # return the new string
    return secretWord

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

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    numGuesses = 8 # number of guesses given to player
    lettersGuessed = []
    mistakesMade = 0
    
    # let user know how many letters the word contains
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    
    # keep playing until it's guessed or out of guesses
    while isWordGuessed(secretWord, lettersGuessed) == False \
        and (numGuesses - mistakesMade) > 0:
        print('-------------')
        print('You have', numGuesses - mistakesMade, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        userGuess = input('Please guess a letter: ')
        userGuess = str(userGuess[0].lower())
        # and index0 to limit it down to one character
        # check to see if it's already been guessed
        if userGuess in lettersGuessed:
            print("Oops! You've already guessed that letter: ", \
                  getGuessedWord(secretWord, lettersGuessed))
            continue
        lettersGuessed.append(userGuess) # because lists are mutable!
        if userGuess in secretWord:
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        else:
            mistakesMade += 1
            print('Oops! That letter is not in my word:', \
                  getGuessedWord(secretWord, lettersGuessed))
    
    # determine if loss or win
    if (numGuesses - mistakesMade) == 0:
        print('-----------')
        print(str('Sorry, you ran out of guesses. The word was ') + secretWord \
              + str('.'))
    else:
        print('-----------')
        print('Congratulations, you won!')
        
# call it to test it
hangman('cat')