THEME_COLOR = "#375362"
from tkinter import *
import quiz_brain as qb

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR)
        self.window.config(padx=20, pady=20)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 13))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150,125, text="placehoder", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=80)

        right_button = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=right_button, highlightthickness=0)
        self.correct_button.grid(row=2, column=0)

        wrong_button = PhotoImage(file="images/false.png")
        self.incorrect_button = Button(image=wrong_button, highlightthickness=0)
        self.incorrect_button.grid(row=2, column=1)

        self.window.mainloop()