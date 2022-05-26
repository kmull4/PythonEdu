'''
In deep.py, implement a program that prompts the user for the answer to the
 Great Question of Life, the Universe and Everything, outputting Yes if the
  user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise
  output No.

Rembmer "42" is a valid string too
'''

# get the user input
userInput = input("What is the answer to the Great Question of Life, the Universe and Everything?")

# make the strings uniform for the string comparison
userInput = userInput.lower()

# if statement with all 3 conditionals (and case insensitive)
# prints yes if true, no if not
if (userInput == "42" or userInput == "forty two" or userInput == "forty-two"):
	print("Yes")
else:
	print("No")