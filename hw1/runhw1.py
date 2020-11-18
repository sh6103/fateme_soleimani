import os
from random import randint

# from  hw1 import *

# The quiz contains 5 questions from the user
from hw1.hw_1 import Score, Quiz, MultipleChoice, TrueFalse

file_answer = open("answer.txt", 'r')
file_question = open("question.txt", 'r')
user_score = Score(0)
list_of_question = file_question.readlines()  # List of all designed questions
list_of_answer = file_answer.readlines()  # List of all designed answers
number_of_false, number_of_true = 0, 0  # Number of incorrect answers and Number of correct answers
for counter in range(1, 6):  # counter=Number of questions asked
    if counter == 1:
        i = 1
    elif counter == 2:
        i = 15
    elif counter == 3:
        i = 8
    else:
        i = randint(2, 14)
    questions = list_of_question[i].strip()
    answers = list_of_answer[i].strip().split(".")
    quiz = Quiz(questions, answers)
    print("Question No.{}:{}".format(counter, quiz))
    if i < 6:
        print(MultipleChoice(questions, i))
    elif 5 < i < 11:
        print(TrueFalse(questions, answers))
    user_answer = input("your answer:")
    if user_answer == " " or user_answer == "":  # The user does not enter anything
        user_score += 0
    elif quiz.check(user_answer):  # The user enters the correct answer
        print("Correct answer")
        user_score += 10
        number_of_true += 1
    else:  # The user enters the incorrect answer
        print("Wrong answer")
        user_score -= 3
        number_of_false += 1
    print("questions asked:{}\t\tcorrect answer:{}\t\twrong answers:{}\t\t{}".format(counter, number_of_true, number_of_false, user_score))
    print("---------------------------------------")
    os.system('cls')

print(user_score)
user_score.check_status()
print(user_score.status)
