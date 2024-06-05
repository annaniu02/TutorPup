import tkinter as tk
from tkinter import ttk

import home
import help
import feedback
import question_input

HEADERFONT = ("Verdana", 40)
LARGEFONT =("Verdana", 30)
MEDIUMFONT =("Verdana", 20)
SMALLFONT =("Verdana", 15)
BTNFONT =("Verdana", 35)

# Question Display Page -- where the questions and answer choices 
class displayPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
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
        label = ttk.Label(self, text ="[display question here]",
                          font = LARGEFONT, background = "#f9cb9c",
                          width = 33, anchor="center")
        # putting the grid in its place by using grid
        label.grid(row = 0, column = 0, columnspan = 6, rowspan = 1)

        # display answer choices randomly assigned to sensors [Left, Right, Front]
        left_label = ttk.Label(self, text="LEFT SENSOR:", font=MEDIUMFONT, background = "#f9cb9c")
        left_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        # TODO: button is placeholder --> question answer choices should be displayed once database is implemented
        leftBtn = ttk.Button(self, text ="LEFT", style = 'btn.TButton',
                                command = lambda : controller.show_frame(feedback.feedbackPage))
        leftBtn.grid(row = 1, column = 1)

        front_label = ttk.Label(self, text="FRONT SENSOR:", font=MEDIUMFONT, background = "#f9cb9c")
        front_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        # TODO: button is placeholder --> question answer choices should be displayed once database is implemented
        frontBtn = ttk.Button(self, text ="FRONT", style = 'btn.TButton',
                                command = lambda : controller.show_frame(feedback.feedbackPage))
        frontBtn.grid(row = 2, column = 1)

        right_label = ttk.Label(self, text="RIGHT SENSOR:", font=MEDIUMFONT, background = "#f9cb9c")
        right_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)
        # TODO: button is placeholder --> question answer choices should be displayed once database is implemented
        rightBtn = ttk.Button(self, text ="RIGHT", style = 'btn.TButton',
                                command = lambda : controller.show_frame(feedback.feedbackPage))
        rightBtn.grid(row = 3, column = 1)

        # instructions content
        instructions = ttk.Label(self, text = "Please indicate your answer by pressing the \ncorresponding sensor on the TutorPup",
                                              background='#f9cb9c', font = LARGEFONT, anchor = "center")
        instructions.grid(row = 4, column = 0, columnspan = 6, rowspan = 2)