'''
Fun code to celebrate Mortimer's first "Gotchya" day.
    Calculates how much of Morti's life has been with me.
9/28/21 was adoption date. Birth ~9 weeks prior.
    9 weeks = 63 days for simplicty. DoB not 100% sure. Marks DoB as 7-27-21
'''
import datetime

def perc_of_life_calc(date):
    # do the calc for percentage of life lived, 3 dec places
    return round((date - adoption) / (date - birth), 3)

def standardize_alpha(alpha):
    # if entered a whole number, return float
    if 0 < alpha <= 1:
        return alpha
    elif alpha > 1:
        return standardize_alpha(alpha/100) # recursive function in the wild
    else: # a negative number was put in for some reason
        return abs(standardize_alpha(alpha))

birth = datetime.datetime(2021, 7, 27)
adoption = datetime.datetime(2021, 9, 28)
today = datetime.datetime.now()

perc_of_life = round((today - adoption) / (today - birth), 3) * 100 # for perc

print("As of today, Kyle has been a part of", perc_of_life, \
      "% of Morti's life!")

# next find dates for 95% of his life, 99% of his life
# next make user input for percentage of life

date = birth + datetime.timedelta(days=1)
alpha = standardize_alpha(float(input('What percentage of life to \
                                      calculate?\n')))


# calculate tomorrow and see if that's your alpha
while(perc_of_life_calc(date) < alpha):
    date = date + datetime.timedelta(days=1)

# if above alpha, then break and post. while loop's got it
# tell user
print('On', date, "Kyle will have been part of Morti's life for", alpha*100,\
      '%')