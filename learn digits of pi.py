'''
Yes, it is enunciated "learn digits of pypy"

Original thought: "woah waoh I had an idea and I need to write it down.
I want to memorize more digits of Pi and I'm trying to see if typing it
 over and over on a keypad will make some kind of muscle / memory
 connection. But there isn't any tool like that readily available 
but... but I can make one.
I'ma make a Pi checker. Maybe it'll keep my score over time too."

http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html
	home monitor zoomed in to 500% for the first 62 digits of pi
get some style https://peps.python.org/pep-0008/
'''

digitsOfPi = '3.1415926535897932384626433832795028841971693993751058209749445'
# digits expandable in v2.0
userPlay = True


def iWannaPlayAGame():
	# print the digits of pi to look at. big font, if you can
	print('The first', len(digitsOfPi), 'digts of Pi are', digitsOfPi)
	# ask the user for their input, stored as a string
	muscleMemory = input('Type in that muscle memory!\n')
	
	# compare input to Pi, digit by digit, and keep track of score
	# also set a minimum range so you don't get error
	score = 0
	minRange = min(len(digitsOfPi), len(muscleMemory))
	for i in range(minRange):
		if digitsOfPi[i] == muscleMemory[i]:
			score += 1
	# keep a counter through the loop for each correct one
		# divide this by length of digits above to get percentage

	# print score, all done here!
	print('Your score is', score, 'of', len(digitsOfPi), 'or',
			round(100*score/len(digitsOfPi),1), '%')
	return score


while (userPlay): 
	# call Iwannaplayagame
	iWannaPlayAGame()
	# store the score
	# press enter to play again or q and enter to quit
	# if input='q', PLAY = False
	userInput = input('Press enter to play again or q and enter to quit\n')
	if userInput == 'q':
		break

# maybe also in v2.0, include options to see your stats over time

# thanks for reading my comments, player
print('Thanks for playing, player.')
