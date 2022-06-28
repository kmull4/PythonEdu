'''
These assignments were multiple. Keeping all of the directions here is
impractical. Here is the last one, which is an almagamation of the others.

You'll notice that in Problem 2, your monthly payment had to be a multiple
of $10. Why did we make it that way? You can try running your code locally so
that the payment can be any dollar and cent amount (in other words, the
monthly payment is a multiple of $0.01). Does your code still work? It should,
but
you may notice that your code runs more slowly, especially in cases with very
large balances and interest rates. (Note: when your code is running on our
servers, there are limits on the amount of computing time each submission is
allowed, so your observations from running this experiment on the grading
system might be limited to an error message complaining about too much time
taken.)

Well then, how can we calculate a more accurate fixed monthly payment
than we
did in Problem 2 without running into the problem of slow code? We can make
this program run faster using a technique introduced in lecture - bisection
search!

The following variables contain values as described below:

balance -
the
outstanding balance on the credit card

annualInterestRate - annual interest
rate as a decimal

** For problems such as these, do not include input statements or define
variables we told you would be given. Our automated testing will provide
values for you - so write your code in the following box assuming those
variables are already defined. The code you paste into the following box
should not specify the values for the variables balance, annualInterestRate,
or monthlyPaymentRate
'''
debug = False
if debug:
    # test case 1 numbers provided
    balance, annualInterestRate = 320000, 0.2

# function to calculate if the minimum payment number will work or not
def year_calculator(balance, paymentAmount):
    for i in range(12):
        balance -= paymentAmount
        interest = balance * (annualInterestRate / 12)
        balance += interest
    return balance

# lower and upper bounds
lowerBound = balance / 12
upperBound = year_calculator(balance, 0) /12 # calculate max interest then /12

# test payment amounts then bisect
while True:
    paymentAmount = (lowerBound + upperBound) /2
    # base case (ie: it works)
    if -0.01 < year_calculator(balance, paymentAmount) < 0.01:
        break
    elif year_calculator(balance, paymentAmount) < -0.01: # overpaid
        upperBound = paymentAmount
    elif year_calculator(balance, paymentAmount) > 0.01: # underpaid
        lowerBound = paymentAmount
    else:
        print('Something has gone terribly wrong')

# final print
print('Lowest Payment:', round(paymentAmount, 2))