import tkinter as tk
from tkinter import ttk
import random
from json_utils import read_questions_from_file, write_questions_to_file

import home
import help
import feedback_correct
import feedback_incorrect

HEADERFONT = ("Verdana", 40)
LARGEFONT =("Verdana", 30)
MEDIUMFONT =("Verdana", 20)
MEDIUMBOLDFONT = ("Verdana", 20, "bold")
SMALLFONT =("Verdana", 15)
BTNFONT =("Verdana", 35)


questionList = read_questions_from_file()

# Question Display Page -- where the questions and answer choices are displayed
class displayPage(tk.Frame):
    current_question_index = 0
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        
        # Placing the home button that links to home page
        home_icon_path = "images/home_icon.png"
        home_icon = tk.PhotoImage(file=home_icon_path)
        homeBtn = ttk.Button(self, text="HOME", style='btn.TButton', image=home_icon,
                             command=lambda: controller.show_frame(home.homePage))
        homeBtn.image = home_icon
        homeBtn.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NW)

        # Placing the help button that links to help page
        help_icon_path = "images/help_icon.png"
        help_icon = tk.PhotoImage(file=help_icon_path)
        helpBtn = ttk.Button(self, text="HELP", style='btn.TButton', image=help_icon,
                             command=lambda: controller.show_frame(help.helpPage))
        helpBtn.image = help_icon
        helpBtn.grid(row=0, column=5, padx=10, pady=10, sticky=tk.NE)

        # Label of header
        self.question_label = ttk.Label(self, text="", font=LARGEFONT, background="#f9cb9c",
                                        width=33, anchor="center")
        self.question_label.grid(row=0, column=0, columnspan=6, rowspan=1)

        # Display answer choices randomly assigned to sensors [Left, Right, Front]
        self.left_label = ttk.Label(self, text="LEFT SENSOR:", font=MEDIUMBOLDFONT, background="#f9cb9c")
        self.left_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.left_answer = ttk.Label(self, text="", font=MEDIUMFONT, background="#f9cb9c")
        self.left_answer.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.front_label = ttk.Label(self, text="FRONT SENSOR:", font=MEDIUMBOLDFONT, background="#f9cb9c")
        self.front_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        self.front_answer = ttk.Label(self, text="", font=MEDIUMFONT, background="#f9cb9c")
        self.front_answer.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.right_label = ttk.Label(self, text="RIGHT SENSOR:", font=MEDIUMBOLDFONT, background="#f9cb9c")
        self.right_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)
        self.right_answer = ttk.Label(self, text="", font=MEDIUMFONT, background="#f9cb9c")
        self.right_answer.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        # Instructions content
        instructions = ttk.Label(self, text="Please indicate your answer by pressing the \ncorresponding sensor on the TutorPup",
                                 background='#f9cb9c', font=LARGEFONT, anchor="center")
        instructions.grid(row=4, column=0, columnspan=6, rowspan=1)

        # Answer buttons
        self.leftBtn = ttk.Button(self, text="LEFT", style='btn.TButton',
                                  command=lambda: self.answer_question(self.left_answer.cget("text")))
        self.leftBtn.grid(row=5, column=0, columnspan=2)
        self.frontBtn = ttk.Button(self, text="FRONT", style='btn.TButton',
                                   command=lambda: self.answer_question(self.front_answer.cget("text")))
        self.frontBtn.grid(row=5, column=2, columnspan=2)
        self.rightBtn = ttk.Button(self, text="RIGHT", style='btn.TButton',
                                   command=lambda: self.answer_question(self.right_answer.cget("text")))
        self.rightBtn.grid(row=5, column=4, columnspan=2)

        self.load_question()

    def load_question(self):
        while questionList[displayPage.current_question_index]['status'] == 'TRUE':
            displayPage.current_question_index = (displayPage.current_question_index + 1) % len(questionList)

        current_question = questionList[displayPage.current_question_index]
        print(f"Loading question at index {displayPage.current_question_index}")
        self.display_question_and_answers(current_question)

    def display_question_and_answers(self, question):
        question_text = question['question']
        answers = [question['option_a'], question['option_b'], question['option_c']]
        random.shuffle(answers)

        self.question_label.config(text=question_text)
        self.left_answer.config(text=answers[0])
        self.front_answer.config(text=answers[1])
        self.right_answer.config(text=answers[2])

    def update_question_status(self, updated_question):
        questions = read_questions_from_file()
        for q in questions:
            if q['question'] == updated_question['question']:
                q['status'] = updated_question['status']
                break
        write_questions_to_file(questions)

    def answer_question(self, user_answer):
        current_question = questionList[displayPage.current_question_index]
        correct_answer = current_question['correct_answer']
        is_correct = user_answer == correct_answer

        if is_correct:
            current_question['status'] = 'TRUE'
            self.update_question_status(current_question)
            self.controller.frames[feedback_correct.feedbackCorrectPage].update_feedback(current_question, "CORRECT", correct_answer)
            self.controller.show_frame(feedback_correct.feedbackCorrectPage)
        else:
            questionList.append(questionList.pop(displayPage.current_question_index))
            self.controller.frames[feedback_incorrect.feedbackIncorrectPage].update_feedback(current_question, "INCORRECT", correct_answer)
            self.controller.show_frame(feedback_incorrect.feedbackIncorrectPage)
