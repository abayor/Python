from OOP 1.quiz_brain import Question
from questiondata import question_data
from quiz_brain import Question
question_bank = []

for i in range(len(question_data)):
    text = question_data[i]['text']
    answer= question_data[i]['answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)
print(question_bank)