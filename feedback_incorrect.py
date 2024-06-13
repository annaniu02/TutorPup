'''
Filename: feedback_incorrect.py
Student: Anna Niu, Yuancheng 'Kaleo' Cao, Tracy Truong
Email: afniu@ucsd.edu, yuc094@ucsd.edu, trtruong@ucsd.edu
Final Project: TutorPup

Description: This file creates the GUI for incorrect answer feedback.
It will display the question at the top of the screen, the term "Incorrect"
in the middle of the screen, and the correct answer at the bottom.
There is a button to continue to the next question in the question deck.
The audio/growling.mp3 audio will play when this screen appears.
'''

import tkinter as tk
from tkinter import ttk


import home
import help
import question_display
import question_input
import finish

# imports for audio
import playsound as ps
import time

import threading

HEADERFONT = ("Verdana", 40)
LARGEFONT =("Verdana", 30)
MEDIUMFONT =("Verdana", 20)
SMALLFONT =("Verdana", 15)
BTNFONT =("Verdana", 35)

questionList = None
# Feedback Page -- once user answer question by pressing corresponding sensor, this page displays to say if answer is right or wrong
class feedbackIncorrectPage(tk.Frame):
    ###
    # Name: __init__(self, parent, controller)
    # Purpose: This function will initialize the feedbackIncorrectPage GUI screen
    # @input: parent (The parent container), controller (The main application controller)
    # @return: None
    ###
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        ###
        # Name: update_feedback(question, feedback, correct_answer)
        # Purpose: This function will update the feedbackIncorrectPage GUI screen with
        #          the current question, the feedback label, and the correct answer.
        # @input: question (The current question), feedback (The feedback label: "INCORRECT"),
        #         correct_answer (The current question's correct answer)
        # @return: None
        ###
        def update_feedback(question, feedback, correct_answer):
            question_label.config(text=question['question'])
            feedback_label.config(text=feedback)
            correction.config(text=f"Correct Answer is: {correct_answer}")

        self.update_feedback = update_feedback

        ###
        # Name: continue_to_next_question()
        # Purpose: This function will load the next question if there are still questions
        #          in the deck, but will proceed to the finishPage if all questions have been
        #          answered correctly in the deck.
        # @input: None
        # @return: None
        ###
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
                          anchor="center")
        # putting the grid in its place by using grid
        question_label.grid(row = 0, column = 0, columnspan = 6, rowspan = 1)

        # feedback label indicates whether user got question CORRECT or INCORRECT
        feedback_label = ttk.Label(self, text ="CORRECT/INCORRECT",
                             font = HEADERFONT, background = "#f9cb9c",
                          width = 33, anchor="center")
        # putting the grid in its place by using grid
        feedback_label.grid(row = 1, column = 0, columnspan = 6, rowspan = 2)

        # correction content
        # displays the correct answer for the current question
        correction = ttk.Label(self, text ="Correct Answer is:",
                               font = LARGEFONT, background = "#f9cb9c",
                               anchor="center")
        correction.grid(row = 3, column = 0, columnspan = 6, rowspan = 2)
        
        # Place CONTINUE button to move to next question display slide
        continueBtn = ttk.Button(self, text ="CONTINUE", style = 'btn.TButton',
                                command = continue_to_next_question)
        continueBtn.grid(row = 5, column = 0, columnspan = 6, rowspan = 1)

        # Create an audio thread
        self.audioThread = None        
            
    ###
    # Name: textToAudio(self)
    # Purpose: Play growling audio
    # @input  None
    # @return None
    ##### 
    def textToAudio(self):
        audioFile = "audio/growling.mp3"
        ps.playsound(audioFile)
    
    ###
    # Name: playAudioThread(self)
    # Purpose: Starts audio thread
    # @input  None
    # @return None
    #####      
    def playAudioThread(self):
        # If an audio thread is currently running, don't start another thread
        if self.audioThread and self.audioThread.is_alive():
            # Wait for previous audio thread to finish
            self.audioThread.join()
        print("new audio thread created for growling audio")
        # Create an audio thread
        self.audioThread = threading.Thread(target=self.textToAudio, args=())
        self.audioThread.start()	# Begin audio thread
        self.checkAudioThread()		# Check if audio thread completed
    
    ###
    # Name: checkAudioThread(self)
    # Purpose: Checks if thread has closed
    # @input  None
    # @return None
    #####       
    def checkAudioThread(self):
        # Check if audio thread alive
        if self.audioThread and self.audioThread.is_alive():
            # Schedule next check after 100 ms
            self.after(100, self.checkAudioThread)
        else:
            print("growling audio thread done")