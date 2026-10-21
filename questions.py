# William Keilsohn
# June 12 2026

# Import Packages
import os
import numpy as np
import pandas as pd
import random
from random import randint, shuffle

## Import Custom Packages
from word_file_loader import df

# Declare Variables
total_questions = len(df)
all_question_range = list(range(0, total_questions)) # Const
ans_options = {x: df.loc[x, 'Meaning'] for x in all_question_range}
que_options = {x: df.loc[x, 'Kanji'] + ' - ' + df.loc[x, 'Furigana'] if pd.notna(df.loc[x, 'Kanji']) else df.loc[x, 'Furigana'] for x in all_question_range}

# Define Functions

def createQuestion(num):
    global ans_options
    global total_questions
    ans = {num: ans_options.get(num)}
    opt1 = {False: ans_options.get(randint(0, total_questions  - 1))}
    opt2 = {False: ans_options.get(randint(0, total_questions  - 1))}
    opt3 = {False: ans_options.get(randint(0, total_questions  - 1))}
    return [ans, opt1, opt2, opt3]
    
def askQuestion(que_vals):
    global que_options
    num = list(que_vals[0].keys())[0]
    word = que_options.get(num)
    shuffle(que_vals)
    q_letters = ['A', 'B', 'C', 'D']
    display_dic = {q_letters[x]: que_vals[x] for x in range(0, len(q_letters))} 
    print('Select the meaning of: {}'.format(word))
    for key, value in display_dic.items():
        e_meaning = next(iter(value.values()))
        possible_ans = '{}: {}'.format(key, e_meaning)
        print(possible_ans)
    user_ans = input('Please select an option: ') # User should enter a single letter. Standard multiple choice format
    return (user_ans.upper(), display_dic)
    
def processAns(quest_tup):
    user_ans = quest_tup[0]
    possible_ans = quest_tup[1]
    user_selection = possible_ans.get(user_ans)
    if type(next(iter(user_selection))) is int:
        print('Correct')
        return (next(iter(user_selection)), True)
    else:
        print('Incorrect')
        for key, value in possible_ans.items():
            if type(next(iter(value))) is int:
                return (next(iter(value)), False)
    
def questionProcess(num):
    que_vals = createQuestion(num=num)
    quest_tup = askQuestion(que_vals=que_vals)
    return processAns(quest_tup=quest_tup)
    
# # Run Application (Testing Only)
# if __name__ == '__main__':
    # num = randint(0, total_questions)
    # print(questionProcess(num=num)) 