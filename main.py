# William Keilsohn
# June 12 2026

# Import Packages
from random import choice

## Import Custom Packages
from questions import *

# Declare Variables
unanswered_questions = list(range(0, total_questions)) # Var
wrong_questions = []
correct_questions = []
questions_remaining = unanswered_questions + wrong_questions
question_checker = len(questions_remaining)

# Run Application
if __name__ == '__main__':
    num = randint(0, total_questions)
    ans_ques = 0
    while question_checker > 0:
        try:
            ans_tup = questionProcess(num=num)
            ans_ques = ans_ques + 1
            if ans_tup[1] == True:
                unanswered_questions.remove(ans_tup[0])
                correct_questions.append(ans_tup[0])
            else:
                wrong_questions.append(ans_tup[0])
            questions_remaining = unanswered_questions + wrong_questions
            question_checker = len(questions_remaining)
            num = choice(questions_remaining)
        except:
            question_checker = 0
    correct_ans = len(correct_questions)
    per_cor = round(correct_ans / ans_ques, 4) * 100 # Divide by zero if you don't answer any questions... lazy...
    print('You got {} out of {} questions correct or about {}%'.format(correct_ans, ans_ques, per_cor))
    