class QuizBrain:
    def __init__(self,quiz_list):
        self.number = 0
        self.score = 0
        self.question_list = quiz_list

    def next_question(self):
        self.current_question = self.question_list[self.number]
        self.number += 1
        user_answer = input(f"Q.{self.number}: {self.current_question.text}. (True / False): ")
        self.check_answer(user_answer)

    def check_answer(self,user_answer):
        if user_answer.lower() == self.current_question.answer.lower():    
            print(f"You got it right!")
            self.score +=1
        else: print("You got lose")
        print(f"The correct answer was: {user_answer}")
        print(f'Your current is:{self.number}/{self.score}\n')
    
    def still_has_question(self):
        return self.number < len(self.question_list)
    
