from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self,quiz:QuizBrain):
        self.quiz = quiz
        self.screen = Tk()
        self.screen.title("Quizzler")
        self.screen.config(padx = 20, pady = 20,bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0",fg="white",bg=THEME_COLOR, font=("Arial",15,"italic"))
        self.score_label.grid(column=1,row=0)

        self.background = Canvas(width=300,height=250,bg="white")
        self.question_text = self.background.create_text(150,125,text="",font=("Arial",20,"italic"), width = 280,fill=THEME_COLOR)
        self.background.grid(column=0,row=1,columnspan=2,pady=50)
        
        true_button_image = PhotoImage(file="/Users/user/OneDrive/바탕 화면/language/python 학습자료/quizzler-app-start/images/true.png")
        false_button_image = PhotoImage(file="/Users/user/OneDrive/바탕 화면/language/python 학습자료/quizzler-app-start/images/false.png")
        self.true_button = Button(image=true_button_image,bg=THEME_COLOR,command=self.is_true)
        self.false_button = Button(image=false_button_image,bg=THEME_COLOR,command=self.is_false)

        self.true_button.grid(column=0,row=2)
        self.false_button.grid(column=1,row=2)

        self.change_question()

        self.screen.mainloop()

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
                         
    def is_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def change_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.background.itemconfig(self.question_text,text=q_text)
        else:
            self.background.itemconfig(self.question_text,text="You've reached the end")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.background.config(bg="green")
        else:
            self.background.config(bg="red")
        self.score_label.config(text=f"Score :{self.quiz.score}")
        self.screen.after(1000,self.change_background_color)
        self.change_question()

    def change_background_color(self):
        self.background.config(bg="white")
    