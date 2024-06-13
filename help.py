'''
Filename: help.py
Student: Anna Niu, Yuancheng 'Kaleo' Cao, Tracy Truong
Email: afniu@ucsd.edu, yuc094@ucsd.edu, trtruong@ucsd.edu
Final Project: TutorPup

Description: This file creates the GUI for the helpPage screen, which is shown
when users select the "Help" icon. This pagee lists the instructions for how to use
TutorPup.
'''

import tkinter as tk
from tkinter import ttk

import home

HEADERFONT = ("Verdana", 40)
LARGEFONT =("Verdana", 30)
MEDIUMFONT =("Verdana", 20)
SMALLFONT =("Verdana", 15)
BTNFONT =("Verdana", 35)

# Help Page -- gives instructions on how to use the TutorPup
class helpPage(tk.Frame):
    ###
    # Name: __init__(self, parent, controller)
    # Purpose: This function will initialize the helpPage GUI screen
    # @input: parent (The parent container), controller (The main application controller)
    # @return: None
    ###
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
                                command = lambda : controller.show_frame(helpPage))
        helpBtn.image = help_icon
        helpBtn.grid(row = 0, column = 5, padx = 10, pady = 10, sticky = tk.NE)

        # label of header
        label = ttk.Label(self, text ="How to Use Your TutorPup!",
                          font = LARGEFONT, background = "#f9cb9c",
                          width = 33, anchor="center")
        # putting the grid in its place by using grid
        label.grid(row = 0, column = 0, columnspan = 6, rowspan = 1)

        # instructions content
        instructions = ttk.Label(self, text = "TutorPup is your favorite interactive study buddy! \n \n"
                                              "1. From the home page, press the START button to begin adding questions. \n"
                                              "    a. Input each question and three possible answer choices (only one is correct!) \n"
                                              "    b. Tell TutorPup which answer choice is correct by inputting the associated letter \n        in the 'Correct Answer' box. \n"
                                              "    c. Click the ADD button to add your question to the deck! \n       Continue adding as many questions as you want. \n"
                                              "    d. Click the DONE button when finished adding questions to begin your study session! \n"
                                              "2. As you begin your study session, press the associated touch sensor on TutorPup to \n     indicate your answer choice for the displayed question. \n"
                                              "    a. RIGHT and LEFT refer to TutorPup's right and left \n"
                                              "    b. Questions answered incorrectly are repeated until all questions are answered correctly. \n"
                                              "3. At the end of the question deck, you'll have the option to RESET or REPLAY. \n"
                                              "    a. RESET: start over from the home page and input new questions/answers \n"
                                              "    b. REPLAY: retest yourself using the current question deck \n"
                                              "4. Press the HOME button in the top left to navigate to the home page. \n"
                                              "5. Press the HELP button in the top right to navigate to this tutorial page.",
                                              background='#f9cb9c', font = MEDIUMFONT, anchor = "center")
        instructions.grid(row = 1, column = 0, columnspan = 6, rowspan = 5)