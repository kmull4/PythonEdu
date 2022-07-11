'''
In Problem 1, we computed an exponential by iteratively executing successive
 multiplications. We can use the same idea, but in a recursive function.

Write a function recurPower(base, exp) which computes  by recursively calling
 itself to solve a smaller version of the same problem, and then multiplying
 the result by base to solve the initial problem.

This function should take in two values - base can be a float or an integer;
 exp will be an integer . It should return one numerical value. Your code must
 be recursive - use of the ** operator or looping constructs is not allowed.
'''

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # https://www.w3schools.com/python/gloss_python_function_recursion.asp
    # w3 saves the day again
    # or maybe a total += whatever the previous function returned?
    debug = False
    total = 1
    
    if debug:
        print('base =', base, 'exp =', exp)
    
    # while exp is still positive, keep recurring
    if exp > 0:
        total = base * recurPower(base, exp -1)

    # on the final return, exp should be 0
    return total


# test
print('\nfinal print', recurPower(5,3))