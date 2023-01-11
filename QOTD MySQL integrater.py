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

# fetch the question function
def get_question_and_answer(date):
    '''
    Takes in date and returns the question and all associated answers.

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
        proof_read = input('Proof read looks good? (y/n)').lower()
        if proof_read == 'y':
            # enter into db
            # print previous year's questions
            print('Thanks for your answer! The previous years you answered:')
            pass
        elif proof_read == 'n':
            # start at the top of this function. is there a command for that?
            pass
        else:
            raise # raise an input error to restart try loop
    
    

# =============================================================================
# Menu & altering or viewing previous questions.
# =============================================================================
