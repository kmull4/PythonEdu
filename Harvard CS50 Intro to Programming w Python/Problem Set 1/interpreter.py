'''
In a file called interpreter.py, implement a program that prompts the
 user for an arithmetic expression and then calculates and outputs
  the result as a floating-point value formatted to one decimal place.
   Assume that the user’s input will be formatted as x y z, with one
    space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer

For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!
'''

# start with the user input
expression = input('What is your arithmetic expression?')

# using an index to parse the string worked in the last
#  problem, let's try that one agian!
index = 0
while 1:
    if expression[index] == ' ':
        break
    else:
        index += 1
# when expression[index] == space, then assign the first part
int1 = int(expression[0:index])
# the next index should only be one character after one
#  space per instructions
index += 1 # move from space to operator
operator = expression[index]
index += 2 # move on to start of next int
# the remaining after the space is int2
int2 = int(expression[index:])

# I suppose just a big if / elif / elif / else here
if operator == '+':
    print(int1 + int2)
elif operator == '-':
    print(int1 - int2)
elif operator == '*':
    print(int1 * int2)
else: # has to be divide, instructions say round 1 dec
    print(round(int1 / int2, 1))
