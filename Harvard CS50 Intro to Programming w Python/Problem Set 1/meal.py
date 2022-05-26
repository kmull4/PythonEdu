"""
Suppose that you’re in a country where it’s customary to eat breakfast
 between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner
  between 18:00 and 19:00. Wouldn’t it be nice if you had a program
   that could tell you what to eat when?

In meal.py, implement a program that prompts the user for a time and
 outputs whether it’s breakfast time, lunch time, or dinner time.
  If it’s not time for a meal, don’t output anything at all. Assume
   that the user’s input will be formatted in 24-hour time as
    #:## or ##:##. And assume that each meal’s time range is inclusive.
     For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime
      in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function
 (that can be called by main) that converts time, a str in 24-hour
  format, to the corresponding number of hours as a float. For
   instance, given a time like "7:30" (i.e., 7 hours and 30 minutes),
    convert should return 7.5 (i.e., 7.5 hours).

Recall that a str comes with quite a few methods, including split,
 which separates a str into a list of values, all of which can be
  assigned to variables at once. For instance, if time is a str
   like "7:30", then:
        hours, minutes = time.split(":")
    will assign "7" to hours and "30" to minutes.
"""

def main():
    # ask the user for a time
    myTime = input('What time is it?')
    # call convert() which returns a float
    # if convert is within a time range, output that meal
    if 7 <= convert(myTime) <= 8:
        print('breakfast time')
    elif 12 <= convert(myTime) <= 13:
        print('lunch time')
    elif 18 <= convert(myTime) <= 19:
        print('dinner time')
    # else do nothing, per instructions

def convert(time):
    # input is a string, output is a float
    # use the string.split method
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = float(minutes)
    # return float: hour.(minutes/60)
    return hours+(minutes/60)

if __name__ == "__main__":
    main()