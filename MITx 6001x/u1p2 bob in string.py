'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
 For example, if s = 'azcbobobegghakl', then your program should print
 
 Number of times bob occurs is: 2
 
'''

# s is assumed, only here for testing
# s = 'azcbobobegghakl'

find_bob = 'bob'
num_bobs = 0
counter = 0

for i in s:
    # if next 3 letters in the string = 'bob', then counter += 1
    if s[counter:counter+3] == find_bob:
        num_bobs += 1
    counter += 1
        
print(num_bobs)