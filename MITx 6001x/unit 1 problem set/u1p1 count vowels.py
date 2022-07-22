'''
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, 
if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
'''

vowels = ['a', 'e', 'i', 'o', 'u']
numVowels = 0

for l in s:
    if l in vowels:
        numVowels += 1

print(numVowels)