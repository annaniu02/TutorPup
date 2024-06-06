import tkinter as tk
from tkinter import ttk


import home
import help
import question_display
import question_input
import finish

HEADERFONT = ("Verdana", 40)
LARGEFONT =("Verdana", 30)
MEDIUMFONT =("Verdana", 20)
SMALLFONT =("Verdana", 15)
BTNFONT =("Verdana", 35)

questionList = None
# Feedback Page -- once user answer question by pressing corresponding sensor, this page displays to say if answer is right or wrong
class feedbackIncorrectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def update_feedback(question, feedback, correct_answer):
            question_label.config(text=question['question'])
            feedback_label.config(text=feedback)
            correction.config(text=f"Correct Answer is: {correct_answer}")

        self.update_feedback = update_feedback

        def continue_to_next_question():
            # controller.frames[question_display.displayPage].load_question()
            controller.show_frame(question_display.displayPage)
        
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
        question_label = ttk.Label(self, text ="[display question here]",
                          font = LARGEFONT, background = "#f9cb9c",
                          width = 33, anchor="center")
        # putting the grid in its place by using grid
        question_label.grid(row = 0, column = 0, columnspan = 6, rowspan = 1)

        # TODO: this should change depending on if the correct sensor was pressed or not
        feedback_label = ttk.Label(self, text ="CORRECT/INCORRECT",
                             font = HEADERFONT, background = "#f9cb9c",
                          width = 33, anchor="center")
        # putting the grid in its place by using grid
        feedback_label.grid(row = 1, column = 0, columnspan = 6, rowspan = 2)

        # correction content
        # TODO: this should change depending on what the correct answer & associated sensor is
        correction = ttk.Label(self, text ="Correct Answer is:",
                               font = LARGEFONT, background = "#f9cb9c",
                          width = 33, anchor="center")
        correction.grid(row = 3, column = 0, columnspan = 6, rowspan = 2)
        
        # Place CONTINUE button to move to next question display slide
        # TODO: normally should display next question, for now have it go to finish page
        continueBtn = ttk.Button(self, text ="CONTINUE", style = 'btn.TButton',
                                command = continue_to_next_question)
        continueBtn.grid(row = 5, column = 0, columnspan = 6, rowspan = 1)