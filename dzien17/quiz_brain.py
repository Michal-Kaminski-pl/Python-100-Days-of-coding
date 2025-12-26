# asking the questions
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list 
        self.score = 0
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number}.Q : {self.current_question.text} (True/False?):\n").capitalize()
        self.check_answer(user_answer, current_answer= self.current_question.answer) 
    
    def check_answer(self, user_answer, current_answer):
        if user_answer == current_answer:
            self.score += 1
            print("Dobrze!\n")
        elif user_answer != current_answer:
            print(f"zle! \n")
        print(f"poprawna odpowiedz to: {current_answer} \ntwoj wynik wynosi {self.score}/{self.question_number}\n \n")


