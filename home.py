'''
Filename: home.py
Student: Anna Niu, Yuancheng 'Kaleo' Cao, Tracy Truong
Email: afniu@ucsd.edu, yuc094@ucsd.edu, trtruong@ucsd.edu
Final Project: TutorPup

Description: This file creates the GUI for the homePage screen, which is shown
at application start up. There is a Help icon in the upper right corner to navigate
to the helpPage screen, and a Home icon in the upper left corner to naviaget back to this
homePage screen. There is a Start button which navigates to the displayPage screen, which
allows users to begin inputting questions. The audio/welcome.mp3 audio will play when this
screen appears for the first time.
'''

import tkinter as tk
from tkinter import ttk
from tkinter import *

import question_input
import help

# imports for audio
from gtts import gTTS
import playsound as ps
import time

import threading

HEADERFONT = ("Verdana", 45)
LARGEFONT =("Verdana", 35)
MEDIUMFONT =("Verdana", 25)
SMALLFONT =("Verdana", 15)
BTNFONT =("Verdana", 35)

# Home Page -- first window frame startpage. Guides user to question_input page to begin adding questions
class homePage(tk.Frame):
    ###
	# Name: __init__(self, parent, controller)
	# Purpose: This function will initialize the homePage GUI screen
	# @input: parent (The parent container), controller (The main application controller)
	# @return: None
	###
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # styles
        labelStyle = ttk.Style()
        labelStyle.theme_use('classic')
        labelStyle.configure('header.TLabel', foreground = "white", background="#f9cb9c",
                             height = 30, width = 30, font = LARGEFONT, anchor = "center")
        
        btnStyle = ttk.Style()
        btnStyle.configure('btn.TButton', foreground = "white", background = "#783f04",
                           highlightthickness=0, height = 30, font = LARGEFONT)

        imgStyle = ttk.Style()
        imgStyle.configure('img.TLabel', background = "#f9cb9c")

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
                             command = lambda : controller.show_frame(homePage))
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
        label = ttk.Label(self, text ="Welcome to TutorPup:\nYour favorite study pal!",
                          font = LARGEFONT, background = "#f9cb9c",
                          width = 33, anchor="center")
        # putting the grid in its place by using grid
        label.grid(row = 0, column = 1, columnspan = 4, rowspan = 1)

        # instructions content 
        instructions = ttk.Label(self, text = "Press the HELP button in the top right for instructions.\n\n"
                                                "Otherwise, press START below to begin adding questions. \n",
                                              background='#f9cb9c', font = MEDIUMFONT, anchor = "center")
        instructions.grid(row = 1, column = 1, columnspan = 4, rowspan = 1)

        # Placing the start button that links to question input page
        startBtn = ttk.Button(self, text ="START", style = 'btn.TButton',
                                command = lambda : controller.show_frame(question_input.inputPage))
        startBtn.grid(row = 2, column = 1, columnspan = 4, rowspan = 1)

        # Create an audio thread, then call the function to start it
        self.audioThread = None
        self.playAudioThread()
        
            
    ###
    # Name: textToAudio(self, text)
    # Purpose: Convert a string into audio
    # @input  text (string that will be converted into an mp3 audio file)
    # @return None
    #####    
    def textToAudio(self, text):
        tts = gTTS(text=text, lang='en')	# Convert the text to speech
        audioFile = "audio/welcomeAudio.mp3"	# Save audio as temp file
        tts.save(audioFile)
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
        print("new audio thread created for welcome")
        # Create an audio thread
        self.audioThread = threading.Thread(target=self.textToAudio, args=("Welcome to TutorPup, your favorite study pal!",))
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
            print("welcome audio thread done")