import tkinter as tk
from tkinter import ttk
import random
from json_utils import read_questions_from_file, write_questions_to_file

import home
import help
import feedback_correct
import feedback_incorrect
import finish
import question_input

HEADERFONT = ("Verdana", 40)
LARGEFONT =("Verdana", 30)
MEDIUMFONT =("Verdana", 20)
MEDIUMBOLDFONT = ("Verdana", 20, "bold")
SMALLFONT =("Verdana", 15)
BTNFONT =("Verdana", 35)

global questionList
questionList = read_questions_from_file()

current_question_index = None
current_question = None

question_text = None
answer_one = None
answer_two = None
answer_three = None

answer_to_sensor = None

# Question Display Page -- where the questions and answer choices 
class displayPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def load_question():
            global current_question_index
            current_question_index = 0
            while questionList[current_question_index]['status'] == 'TRUE':
                current_question_index = (current_question_index + 1) % len(questionList)
        
            print(current_question_index)
            
            global current_question
            current_question = questionList[current_question_index]
            display_question_and_answers(current_question)
        

        def display_question_and_answers(question):
            global question_text 
            question_text = question['question']
            answers = [question['option_a'], question['option_b'], question['option_c']]
            random.shuffle(answers)

            global answer_one
            answer_one = answers[0]

            global answer_two
            answer_two = answers[1]

            global answer_three
            answer_three = answers[2]
           
            global answer_to_sensor
            answer_to_sensor = {
                'Left': answers[0],
                'Front': answers[1],
                'Right': answers[2]
            }

            print(f"Question: {question_text}")
            print(f"Left: {answers[0]}, Front: {answers[1]}, Right: {answers[2]}")

        def update_question_status(updated_question):
            questions = read_questions_from_file()
            for q in questions:
                if q['question'] == updated_question['question']:
                    q['status'] = updated_question['status']
                    break
            write_questions_to_file(questions)


        def answer_question(user_answer):
            correct_answer = current_question['correct_answer']
            is_correct = user_answer == correct_answer

            if is_correct:
                feedback = "CORRECT"
                current_question['status'] = 'TRUE'
                update_question_status(current_question)
                controller.frames[feedback_correct.feedbackCorrectPage].update_feedback(current_question, "CORRECT", current_question['correct_answer'])
                # feedback_correct.feedbackCorrectPage.update_feedback(current_question, feedback, correct_answer)
                controller.show_frame(feedback_correct.feedbackCorrectPage)
            else:
                feedback = "INCORRECT"
                questionList.append(questionList.pop(current_question_index))
                controller.frames[feedback_incorrect.feedbackIncorrectPage].update_feedback(current_question, "INCORRECT", current_question['correct_answer'])
                #feedback_incorrect.feedbackIncorrectPage.update_feedback(current_question, feedback, correct_answer)
                controller.show_frame(feedback_incorrect.feedbackIncorrectPage)


        load_question()

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
        home_icon = tk.PhotoImage(file = home_icon_path)
        homeBtn = ttk.Button(self, text="HOME", style = 'btn.TButton', image = home_icon,
                             command = lambda : controller.show_frame(home.homePage))
        homeBtn.image = home_icon
        homeBtn.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.NW)

        # Placing the help button that links to help page
        help_icon_path = "images/help_icon.png"
        help_icon = tk.PhotoImage(file = help_icon_path)
        helpBtn = ttk.Button(self, text ="HELP", style = 'btn.TButton', image = help_icon,
                                command = lambda : controller.show_frame(help.helpPage))
        helpBtn.image = help_icon
        helpBtn.grid(row = 0, column = 5, padx = 10, pady = 10, sticky = tk.NE)

        # label of header
        question_label = ttk.Label(self, text = question_text,
                          font = LARGEFONT, background = "#f9cb9c",
                          width = 33, anchor="center")
        # putting the grid in its place by using grid
        question_label.grid(row = 0, column = 0, columnspan = 6, rowspan = 1)

        # display answer choices randomly assigned to sensors [Left, Right, Front]
        left_label = ttk.Label(self, text="LEFT SENSOR:", font=MEDIUMBOLDFONT, background = "#f9cb9c")
        left_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        # TODO: button is placeholder --> question answer choices should be displayed once database is implemented
        # leftBtn = ttk.Label(self, text ="LEFT", style = 'btn.TButton',
        #                         command = lambda : controller.show_frame(feedback.feedbackPage))
        # leftBtn.grid(row = 1, column = 1)
        left_answer = ttk.Label(self, text=answer_one, font=MEDIUMFONT, background="#f9cb9c")
        left_answer.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        front_label = ttk.Label(self, text="FRONT SENSOR:", font=MEDIUMBOLDFONT, background = "#f9cb9c")
        front_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        # TODO: button is placeholder --> question answer choices should be displayed once database is implemented
        # frontBtn = ttk.Button(self, text ="FRONT", style = 'btn.TButton',
        #                         command = lambda : controller.show_frame(feedback.feedbackPage))
        # frontBtn.grid(row = 2, column = 1)
        front_answer = ttk.Label(self, text=answer_two, font=MEDIUMFONT, background="#f9cb9c")
        front_answer.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        right_label = ttk.Label(self, text="RIGHT SENSOR:", font=MEDIUMBOLDFONT, background = "#f9cb9c")
        right_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)
        # TODO: button is placeholder --> question answer choices should be displayed once database is implemented
        # rightBtn = ttk.Button(self, text ="RIGHT", style = 'btn.TButton',
        #                         command = lambda : controller.show_frame(feedback.feedbackPage))
        # rightBtn.grid(row = 3, column = 1)
        right_answer = ttk.Label(self, text=answer_three, font=MEDIUMFONT, background="#f9cb9c")
        right_answer.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        # instructions content
        instructions = ttk.Label(self, text = "Please indicate your answer by pressing the \ncorresponding sensor on the TutorPup",
                                              background='#f9cb9c', font = LARGEFONT, anchor = "center")
        instructions.grid(row = 4, column = 0, columnspan = 6, rowspan = 1)

        # answer buttons -- PLACEHOLDER
        leftBtn = ttk.Button(self, text ="LEFT", style = 'btn.TButton',
                                command = lambda : answer_question(left_answer.cget("text")))
        leftBtn.grid(row = 5, column = 0, columnspan = 2)
        frontBtn = ttk.Button(self, text ="FRONT", style = 'btn.TButton',
                                command = lambda : answer_question(front_answer.cget("text")))
        frontBtn.grid(row = 5, column = 2, columnspan = 2)
        rightBtn = ttk.Button(self, text ="RIGHT", style = 'btn.TButton',
                                command = lambda : answer_question(right_answer.cget("text")))
        rightBtn.grid(row = 5, column = 4, columnspan = 2)
    