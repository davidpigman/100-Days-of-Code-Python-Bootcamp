class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_right = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
    #print(f"question_text {question_text.text}")

        if user_answer == question.answer:
            print("You got it right!")
            print(f"The correct answer was {question.answer}.")
            self.question_right += 1
        else:
            print("That's wrong!")
        
        print(f"Your current score is {self.question_right}/{self.question_number}")
        print("\n")

    


