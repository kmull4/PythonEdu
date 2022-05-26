"""
In a file called faces.py, implement a function called convert that accepts a str as input
and returns that same input with any :) converted to 🙂 (otherwise known as a
slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face).
All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input,
calls convert on that input, and prints the result. You’re welcome, but not required, to
prompt the user explicitly, as by passing a str of your own as an argument to input. Be
sure to call main at the bottom of your file.
"""

# first function called convert. takes a string, returns a string with :) and :( converted
def convert(mystr):
	# okay so now you have the string floating around... now what to do with it
	# use the replace method to convert the string. Remember, self, that it has to replace something.
	# 	It doesn't just happen on itself.
	mystr = mystr.replace(':)', '🙂') # smileys
	mystr = mystr.replace(':(', '🙁') # sadleys
	# and finally return the string
	return mystr

# second function called main. asks user for a string then passes that to convert. prints what convert returns
def main():
	userinput = input('What string, user?\n')
	print(convert(userinput)) # run convert on the user input and print that
	# the above is printing out what the convert function returns

# ?? what does this even mean?
# You’re welcome, but not required, to prompt the user explicitly, 
# as by passing a str of your own as an argument to input.


# don't forget to call main at the bottom
main()
