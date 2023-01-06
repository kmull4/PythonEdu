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

months = ['January', 'February', 'March', 'April', 'May', 'June',\
          'July', 'August', 'September', 'October', 'November', 'December']
kyleQOTD = 'C:/'
saraQOTD = 'C:/'
testQOTD = 'qotd_test_data.txt'

# =============================================================================
# MySQL interface
# =============================================================================
# TODO: this part

# =============================================================================
# Importing from text file
# =============================================================================
# read text file, parse text, and enter into db
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
    Tuple of:
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
# TODO: also this part

# =============================================================================
# Menu & altering or viewing previous questions.
# =============================================================================
