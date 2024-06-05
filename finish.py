import tkinter as tk
from tkinter import ttk
from json_utils import read_questions_from_file, write_questions_to_file

import home
import help
import question_display
import question_input

HEADERFONT = ("Verdana", 40)
LARGEFONT =("Verdana", 30)
MEDIUMFONT =("Verdana", 20)
SMALLFONT =("Verdana", 15)
BTNFONT =("Verdana", 35)

# Finish Page -- once all questions have been answered correctly, can choose to either RESET (input new questions) or REPLAY (replay question deck)
class finishPage(tk.Frame):
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
        label = ttk.Label(self, text ="CONGRATULATIONS",
                          font = HEADERFONT, background = "#f9cb9c",
                          width = 33, anchor="center")
        # putting the grid in its place by using grid
        label.grid(row = 0, column = 0, columnspan = 6, rowspan = 1)

        # instructions content
        instructions = ttk.Label(self, text = "You have finished studying this question deck. \n"
                                              "    a. If you would like to restart and study new questions, \n        click 'RESET' below \n"
                                              "    b. If you would like to restudy this question deck, \n        click 'REPLAY' below",
                                              background='#f9cb9c', font = LARGEFONT, anchor = "center")
        instructions.grid(row = 1, column = 0, columnspan = 6, rowspan = 4)

        # Place RESET button go back to question_input page
        # TODO: connect this functionality to database
        # TODO: after RESET button clicked, database should be cleared
        # TODO: do we want screen where user can review questions currently in database?
        resetBtn = ttk.Button(self, text ="RESET", style = 'btn.TButton',
                                command = self.resetDatabase)
        resetBtn.grid(row = 5, column = 0, columnspan = 3, rowspan = 1)

        # Place REPLAY button to move to question display slides
        # TODO: connect this functionality to database
        # TODO: after REPLAY button clicked, all questions in database should be run through and answered again --> status of questions back to 'incorrect'
        replayBtn = ttk.Button(self, text ="REPLAY", style = 'btn.TButton',
                                command = self.replayDatabase)
        replayBtn.grid(row = 5, column = 3, columnspan = 3, rowspan = 1)
    
    # TODO: reset database
    def resetDatabase(self):
        questions = read_questions_from_file()
        if questions:
            questions_to_keep = [questions[0]]  # Keep only the first question
            write_questions_to_file(questions_to_keep)
            print("Database reset. Only the first row is kept.")
        else:
            print("No questions found in the JSON file.")

        self.controller.show_frame(question_input.inputPage)
        return
        
    # TODO: replay database
    def replayDatabase(self):
        questions = read_questions_from_file()
        for question in questions:
            question['status'] = 'FALSE'
        write_questions_to_file(questions)
        self.controller.show_frame(question_display.displayPage)
        return