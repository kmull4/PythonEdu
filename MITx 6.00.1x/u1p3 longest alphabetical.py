'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
 occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your
 program should print
     Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd',
 then your program should print
     Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. If
 you've spent more than a few hours on this problem, we suggest that you move
 on to a different part of the course. If you have time, come back to this
 problem after you've had a break and cleared your head. 
'''

debug = False

# s is assumed but here for the debug process
if debug:
    s = 'abcdefghijklmnopqrstuvwxyz'
    print('len of s =', len(s))

# set score, high score, and high score str
score, high_score, high_score_str = 0, 0, s[0]
# counter to keep track of position in loop
counter = 0
# position to keep track of ??
pos = 0

# parse through string and determine if subseqent letters are < str values
for i in s:
    if debug:
        print('i =', i, 'counter =', counter, 'pos =', pos)
    counter = pos
    # for loop to keep proceeding to next letter and setting score
    for j in range(len(s[pos:-1])): # one short of an error
        if s[counter] <= s[counter+1]:
            score += 1
            counter += 1
            if debug:
                print('score =', score, 'counter =', counter)
    # determine high score
    if debug:
        print(high_score)
    if score > high_score:
        high_score = score
        # set high_score_str
        high_score_str = s[pos:pos+score+1]
    # reset score
    score = 0
    # position in string moves
    pos += 1

print('Longest substring in alphabetical order is:', high_score_str)
