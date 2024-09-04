from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#question = Question()
question_bank = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)
quiz_brain_length = len(question_bank)

#print(f"quiz brain length {quiz_brain_length}")

for item in question_bank:  
    question_text = quiz_brain.next_question()

print("You've completed the quiz!")
print(f"Your final score is {quiz_brain.question_right}/{quiz_brain.question_number}.")


