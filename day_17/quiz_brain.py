class QuizBrain:
    def __init__(self, question_list):
        self.q_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        if self.q_number < len(self.question_list):
            return True
        else:    
            return False

    def next_question(self):
        current_question = self.question_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"{self.q_number}: {current_question.text} (True or Flase): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() != str(correct_answer).lower():
            print("Correct")
        else:
            print("Wrong.")