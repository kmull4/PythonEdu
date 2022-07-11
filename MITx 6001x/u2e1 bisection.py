'''
In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 
(inclusive) and 100 (not inclusive). The computer makes guesses, and you give 
it input - is its guess too high or too low? Using bisection search, the
 computer will guess the user's secret number!
 
** Your program should use bisection search. So think carefully what that
 means. What will the first guess always be? How should you calculate
 subsequent guesses?

** Your initial endpoints should be 0 and 100. Do not optimize your
 subsequent endpoints by making them be the halfway point plus or minus
 1. Rather, just make them be the halfway point.
 
Note: your program should use input to obtain the user's input! Be sure to 
handle the case when the user's input is not one of h, l, or c.

When the user enters something invalid, you should print out a message to the
user explaining you did not understand their input. Then, you should re-ask 
the question, and prompt again for input. For example:
"Sorry, I did not understand your input."
'''

# start with high and low variables and valid inputs
low, high = 0, 100
valid_input = ['h', 'l', 'c']

print('Please think of a number between 0 and 100!')

# while loop
while True:
    # calculate guess from last low & high
    guess = int((low + high) / 2)
    # print guess and prompt for user
    print('Is your secret number ' + str(guess) + '?')
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    # check to see if input is valid
    if user_input not in valid_input:
        print('Sorry, I did not understand your input.')
        continue # go back to top
    # if input is 'c', then break
    if user_input == 'c':
        print('Game over. Your secret number was:', guess)
        break
    # if input is l for low, then low = guess
    if user_input == 'l':
        low = guess
    # same for h for high, high = guess
    else:
        high = guess
    # time to go back to top of loop
