'''
The greatest common divisor of two positive integers is the largest integer
that divides each of them without remainder. For example,

gcd(2, 12) =
2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

A clever mathematical trick
(due
to Euclid) makes it easy to find greatest common divisors. Suppose that a and b
are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a,
b) is the same as gcd(b, a % b)

See this website for an example of Euclid's
algorithm being used to find the gcd.

Write a function gcdRecur(a, b) that
implements this idea recursively. This function takes in two positive integers
and
returns one integer.
'''

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # uses euclid's subtraction algorithm situation
    
    # cannot use a function to pick a variable to assign so do it here
    # also a great place to return the answer if it's time
    if a == b or a < 1 or b < 1:
        return b
    elif a < b:
        y = a
        a = b
        b = y
    # now a will be the greater and we know they are not equal
    # higher number % lower number becomes new... one of them number
    return gcdRecur(a % b, b)
    # and then... do that again I guess

# test me
# euclid's 1071 and 462 have a gcd of 21
print(gcdRecur(1071, 462))