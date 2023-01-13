# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:57:23 2022

@author: RedPC

This is my first scratchpad for an integrator that will use MySQL to the
answers to a full year of QOTD (Question Of The Day) questions and answers, as
well as allow the prompting of the day's question and adding it to the
database.
The first year of questions and answers (2022) is stored in a text document
with the structure:
    Month Day[new line]
    Question[new line]
    Answer[new line]
    [two new lines]
"""
import mysql.connector, datetime.datetime

months = ['January', 'February', 'March', 'April', 'May', 'June',\
          'July', 'August', 'September', 'October', 'November', 'December']
kyleQOTD = 'C:/'
saraQOTD = 'C:/'
testQOTD = 'qotd_test_data.txt'

# =============================================================================
# MySQL interface
# =============================================================================
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="qotd_db" # TODO: make the database in mysql
    )

# =============================================================================
# Importing from text file (only used once in establishing db)
# read text file, parse text, and enter into db
# =============================================================================
f = open(testQOTD, 'r')
#header = f.readline().strip().split(',')
count = 0

for line in f:
    #items = line.strip().split('\n')

    # date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
    # year = int(date.group(1))
    # month = int(date.group(2))
    # day = int(date.group(3))

    # city = items[header.index('CITY')]
    # temperature = float(items[header.index('TEMP')])
    # if city not in self.rawdata:
    #     self.rawdata[city] = {}
    # if year not in self.rawdata[city]:
    #     self.rawdata[city][year] = {}
    # if month not in self.rawdata[city][year]:
    #     self.rawdata[city][year][month] = {}
    # self.rawdata[city][year][month][day] = temperature
    count += 1
    
    try:
        if line.split()[0] in months: # this line is a month / day combo
            day = line.split()[1]
            print('month & day are', line)
            questionOrAnswer = 0
            # TODO add to db
        elif questionOrAnswer == 0: # this line is a question
            questionOrAnswer = 1
            print('question:', line)
            # TODO add to db
        elif questionOrAnswer == 1: # this line is an answer
            questionOrAnswer = 0
            print('answer:', line)
            # TODO add to db
    except IndexError: # this is a blank line
        continue
    
    #print('line #', count)
    
    
f.close()

# =============================================================================
# Here and below are functions that are to be used more than once.
# =============================================================================

def print_menu():
    print("Just press enter to go to today's question.\n\
          Enter v to view your q&a for a specific date.\n\
          Enter vo to view other q&a for a specific date.\n\
          Enter e to edit an answer.")
    

# fetch the question function
def get_question_and_answer(date, user):
    '''
    Takes in date and returns the question and all associated answers.
    Assumes the date is usable... or changes it if not.
    datetime.datetime may have an input, or the user may also give an input.
    
    Parameters
    ----------
    date : TYPE
        DESCRIPTION.

    Returns
    -------
    A tuple of:
    question : STR
        The question for that particular day.
    answer : STR
        A list of answers for each year. Maybe a dictionary? Probably a list.
    '''
    pass
    return (question, answer)

# =============================================================================
# Presenting today's question.
# =============================================================================
# datetime.datetime will be used here
def today():
    todays_date = datetime.datetime.today() # TODO: there's no way you did datetime correctly from memory
    todays_question = get_question_and_answer(todays_date[0])
    print("Today's question is:", todays_question)
    todays_answer = input('')
    print("Review of today's answer:", todays_answer)
    try:
        proof_read = input('Proof read looks good? (y/n/q to quit)').lower()
        if proof_read == 'y':
            # enter into db
            # print previous year's questions
            print('Thanks for your answer! The previous years you answered:')
            pass
        elif proof_read == 'n':
            # start at the top of this function. is there a command for that?
            pass
        elif proof_read == 'q':
            # quit the whole function and go back to menu
            pass
        else:
            raise Exception # TODO find what's closest to "inputException"
    except:
        # if at first your input isn't right, try: and try: again
        pass
    

# =============================================================================
# Menu & altering or viewing previous questions.
# =============================================================================
def __main__():
    # TODO: check that you did __main__() right, don't really remember.
    user = input('Who goes there? (s/k)').lower()
    try:
        print_menu()
        menu = input('')
        if menu == '':
            today()
        elif menu == 'v':
            # look up the format of datetime and use date here for that situation
            # put more info on situation in the get_question_and_answer(date)
            # function because that's what needs a specific date input
            view_month = input('What is the month? (number only)')
            view_day = input('What is the day? (number only)')
            view_date = view_month + view_day #TODO some or other. hungry break.
            get_question_and_answer(view_date)
        elif menu == 'vo':
            pass
        elif menu == 'e':
            pass
    except:
        raise Exception # input exception idea again