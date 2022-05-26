'''
In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises
 to give $100 to anyone who isn’t greeted with a “hello.” Kramer is
  instead greeted with a “hey,” which he insists isn’t a “hello,”
   and so he asks for $100. The bank’s manager proposes a compromise:
    “You got a greeting that starts with an ‘h,’ how does $20 sound?”
     Kramer accepts.

In a file called bank.py, implement a program that prompts the user for
 a greeting. If the greeting starts with “hello”, output $0. If the
  greeting starts with an “h” (but not “hello”), output $20. Otherwise,
   output $100. Ignore any leading whitespace in the user’s greeting,
    and treat the user’s greeting case-insensitively.
'''

# get user input for the greeting
greeting = input('Greeting: ').lower()

# check if index 0 == h
if greeting[0] == 'h':
    # if it does, check if index 1-4 == hello
    if greeting[0:5] == 'hello':
        print("$0") # you were properly greeted
    # else, print $20
    else:
        print("$20") # it at least started with an h
# last else, print $100
else:
    print("$100") # didn't even start with an h
