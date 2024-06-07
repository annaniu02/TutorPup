import tkinter as tk
from tkinter import ttk
from database import shared_list, add_item, remove_item, get_list, reset_database

import home
import help
import question_display
import question_input

# imports for audio
import playsound as ps
import time

import threading

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

        # TODO: reset database
        def resetDatabase():

            shared_list.clear()

            print(f"length of question list: {len(shared_list)}")
            question_display.displayPage.current_question_index = 0
            controller.show_frame(question_input.inputPage)
            
        # TODO: replay database
        def replayDatabase():
            for question in shared_list:
                question['status'] = 'FALSE'

            print(f"before: {question_display.displayPage.current_question_index}")
            question_display.displayPage.current_question_index = 0
            print(f"after: {question_display.displayPage.current_question_index}")
            self.controller.show_frame(question_display.displayPage)

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
                                command = resetDatabase)
        resetBtn.grid(row = 5, column = 0, columnspan = 3, rowspan = 1)

        # Place REPLAY button to move to question display slides
        # TODO: connect this functionality to database
        # TODO: after REPLAY button clicked, all questions in database should be run through and answered again --> status of questions back to 'incorrect'
        replayBtn = ttk.Button(self, text ="REPLAY", style = 'btn.TButton',
                                command = replayDatabase)
        replayBtn.grid(row = 5, column = 3, columnspan = 3, rowspan = 1)


        # Create an audio thread
        self.audioThread = None        
            
    ###
    # Name: textToAudio
    # Purpose: Convert a string into audio
    # @input  text (string that will be converted into an mp3 audio file)
    # @return None
    #####  
    def textToAudio(self):
        audioFile = "audio/congratulations.mp3"
        ps.playsound(audioFile)
     
    ###
    # Name: playAudioThread
    # Purpose: Starts audio thread
    # @input  None
    # @return None
    #####      
    def playAudioThread(self):
        # If an audio thread is currently running, don't start another thread
        if self.audioThread and self.audioThread.is_alive():
            # Wait for previous audio thread to finish
            self.audioThread.join()
        print("new audio thread created for congratulatory audio")
        # Create an audio thread
        self.audioThread = threading.Thread(target=self.textToAudio, args=())
        self.audioThread.start()	# Begin audio thread
        self.checkAudioThread()		# Check if audio thread completed
    
    ###
    # Name: checkAudioThread
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
            print("congratulatory audio thread done")
        