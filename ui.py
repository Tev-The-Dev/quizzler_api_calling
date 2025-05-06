THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR)
        self.window.config(padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 13))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150,125, text="Placeholder Text", font=("Arial", 20, "italic"), width=290)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=80)

        right_button = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=right_button, highlightthickness=0, command=self.true_choice)
        self.correct_button.grid(row=2, column=0)

        wrong_button = PhotoImage(file="images/false.png")
        self.incorrect_button = Button(image=wrong_button, highlightthickness=0,command=self.false_choice)
        self.incorrect_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.get_score()}")
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of the quiz. Your final score is {self.quiz.get_score()}")
            self.correct_button.config(state="disabled")
            self.incorrect_button.config(state="disabled")

    def true_choice(self):
        #is_right = self.quiz.check_answer("true")
        self.give_feedback(self.quiz.check_answer("true"))


    def false_choice(self):
        #is_right = self.quiz.check_answer("false")
        self.give_feedback(self.quiz.check_answer("false"))
        #self.update_score()
        #self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
