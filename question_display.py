'''
Filename: question_display.py
Student: Anna Niu, Yuancheng 'Kaleo' Cao, Tracy Truong
Email: afniu@ucsd.edu, yuc094@ucsd.edu, trtruong@ucsd.edu
Final Project: TutorPup

Description: This file creates the GUI for the displayPage screen. It will display
the current question at the top of the screen, the randomized answer options and their
corresponding touch sensor assignments in the middle of the screen, and instructions
for how to answer the question at the bottom of the screen. The question will be read
out loud through the Pupper's speaker system.
'''

import tkinter as tk
from tkinter import ttk
import random
from database import shared_list, add_item, remove_item, get_list

import home
import help
import question_input
import feedback_correct
import feedback_incorrect

# imports for audio
from gtts import gTTS
import playsound as ps
import time

import threading

import time
import RPi.GPIO as GPIO


# There are 4 areas for touch actions
# Each GPIO to each touch area
touchPin_Front = 6
touchPin_Left  = 3
touchPin_Right = 16
touchPin_Back  = 2

# Use GPIO number but not PIN number
GPIO.setmode(GPIO.BCM)

# Set up GPIO numbers to input
GPIO.setup(touchPin_Front, GPIO.IN)
GPIO.setup(touchPin_Left,  GPIO.IN)
GPIO.setup(touchPin_Right, GPIO.IN)
GPIO.setup(touchPin_Back,  GPIO.IN)


HEADERFONT = ("Verdana", 40)
LARGEFONT =("Verdana", 30)
MEDIUMFONT =("Verdana", 20)
MEDIUMBOLDFONT = ("Verdana", 20, "bold")
SMALLFONT =("Verdana", 15)
BTNFONT =("Verdana", 35)

questions = get_list()


# Question Display Page -- where the questions and answer choices are displayed
class displayPage(tk.Frame):
    current_question_index = 0
    controller_ = None  # controller for use outside of init

    currentQuestion_ = None # to be used for audio thread

    ###
	# Name: __init__(self, parent, controller)
	# Purpose: This function will initialize the displayPage GUI screen
	# @input: parent (The parent container), controller (The main application controller)
	# @return: None
	###
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        print("inside the sensor constructor")
        displayPage.controller_ = controller  # instantiate controller_
        
        ###
        # Name: load_question
        # Purpose: Load the questions from question deck, and display the current question if it exists
        # @input  None
        # @return None
        #####
        def load_question():
            while questions and questions[displayPage.current_question_index]['status'] == 'TRUE':
                displayPage.current_question_index = (displayPage.current_question_index + 1) % len(questions)

            if questions:
                current_question = questions[displayPage.current_question_index]
                displayPage.currentQuestion_ = current_question['question']
                print(f"Loading question at index {displayPage.current_question_index}")
                display_question_and_answers(current_question)

        ###
        # Name: display_question_and_answers(question)
        # Purpose: Displays current question in deck, as well as its answer options
        # @input  question (The question being asked to the user)
        # @return None
        #####
        def display_question_and_answers(question):
            question_text = question['question']
            answers = [question['option_a'], question['option_b'], question['option_c']]
            random.shuffle(answers)

            print(question_text)
            self.question_label.config(text=question_text)
            self.left_answer.config(text=answers[0])
            self.front_answer.config(text=answers[1])
            self.right_answer.config(text=answers[2])

        '''
        def update_question_status(updated_question):
            for q in questions:
                if q['question'] == updated_question['question']:
                    q['status'] = updated_question['status']
                    break

        def answer_question(user_answer):
            current_question = questions[displayPage.current_question_index]
            correct_answer = current_question['correct_answer']
            is_correct = user_answer == correct_answer

            if is_correct:
                current_question['status'] = 'TRUE'
                update_question_status(current_question)
                controller.frames[feedback_correct.feedbackCorrectPage].update_feedback(current_question, "CORRECT", correct_answer)
                controller.show_frame(feedback_correct.feedbackCorrectPage)
            else:
                add_item(questions.pop(displayPage.current_question_index))
                controller.frames[feedback_incorrect.feedbackIncorrectPage].update_feedback(current_question, "INCORRECT", correct_answer)
                controller.show_frame(feedback_incorrect.feedbackIncorrectPage)
        '''



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
                                        anchor="center")
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

        '''
        # Answer buttons
        self.leftBtn = ttk.Button(self, text="LEFT", style='btn.TButton',
                                  command=lambda: answer_question(self.left_answer.cget("text")))
        self.leftBtn.grid(row=5, column=0, columnspan=2)
        self.frontBtn = ttk.Button(self, text="FRONT", style='btn.TButton',
                                   command=lambda: answer_question(self.front_answer.cget("text")))
        self.frontBtn.grid(row=5, column=2, columnspan=2)
        self.rightBtn = ttk.Button(self, text="RIGHT", style='btn.TButton',
                                   command=lambda: answer_question(self.right_answer.cget("text")))
        self.rightBtn.grid(row=5, column=4, columnspan=2)
        '''

        ###
        # Name: tkraise_wrapper(aboveThis=None)
        # Purpose: This function calls load_question() every time the widget is raised.
        # @input  aboveThis (The widget that the current widget should be raised above)
        # @return None
        #####    
        def tkraise_wrapper(aboveThis=None):
            load_question()
            tk.Frame.tkraise(self, aboveThis)

        self.tkraise = tkraise_wrapper

        # Create an audio thread
        self.audioThread = None
        # Create an sensor thread
        self.sensorThread = None
    
    ###
    # Name: update_question_status(self, updated_question)
    # Purpose: Updates the status of the updated_question
    # @input  updated_question (The question whose status needs to be updated)
    # @return None
    #####     
    def update_question_status(self, updated_question):
        for q in questions:
            if q['question'] == updated_question['question']:
                q['status'] = updated_question['status']
                break
                    
    ###
    # Name: answer_question(self, user_answer)
    # Purpose: Handles user response from touch sensor, then navigates to appropriate feedback page
    # @input  user_answer (The answer corresponding to the sensor that the user selected)
    # @return None
    ##### 
    def answer_question(self, user_answer):
        current_question = questions[displayPage.current_question_index]
        correct_answer = current_question['correct_answer']
        is_correct = user_answer == correct_answer

        if is_correct:
            current_question['status'] = 'TRUE'
            self.update_question_status(current_question)
            displayPage.controller_.frames[feedback_correct.feedbackCorrectPage].update_feedback(current_question, "CORRECT", correct_answer)
            displayPage.controller_.show_frame(feedback_correct.feedbackCorrectPage)
        else:
            add_item(questions.pop(displayPage.current_question_index))
            displayPage.controller_.frames[feedback_incorrect.feedbackIncorrectPage].update_feedback(current_question, "INCORRECT", correct_answer)
            displayPage.controller_.show_frame(feedback_incorrect.feedbackIncorrectPage)
    
    
    ###
    # Name: receiveSensor(self)
    # Purpose: Detects when user touches a sensor, then calls answer_question to process answer
    # @input  None
    # @return None
    #####     
    def receiveSensor(self):
        while True:
            # Read the state of the touch sensors at the front, left, and right positions
            self.touchValue_Front = GPIO.input(touchPin_Front)
            self.touchValue_Left  = GPIO.input(touchPin_Left)
            self.touchValue_Right = GPIO.input(touchPin_Right)
                
            if not self.touchValue_Left:
                self.answer_question(self.left_answer.cget("text"))
                print("user input: left sensor")
                break
            if not self.touchValue_Right:
                self.answer_question(self.right_answer.cget("text"))
                print("user input: right sensor")
                break
            if not self.touchValue_Front:
                self.answer_question(self.front_answer.cget("text"))
                print("user input: front")
                break
                
            time.sleep(0.5)
    
    ###
    # Name: waitForSensorInputThread(self)
    # Purpose: Starts thread for awaiting sensor input
    # @input  None
    # @return None
    #####      
    def waitForSensorInputThread(self):
        print("inside the sensor thread")
        # If a thread is currently running, don't start another thread
        if self.sensorThread and self.sensorThread.is_alive():
            # Wait for previous  thread to finish
            self.sensorThread.join()
        print("new sensor thread created for question input")
        # Create a thread
        self.sensorThread = threading.Thread(target=self.receiveSensor, args=())
        self.sensorThread.start()	# Begin thread
        self.checkThread()		# Check if thread completed
    
    
    ###
    # Name: checkThread(self)
    # Purpose: Checks if thread has closed
    # @input  None
    # @return None
    #####       
    def checkThread(self):
        # Check if thread alive
        if self.sensorThread and self.sensorThread.is_alive():
            # Schedule next check after 100 ms
            self.after(100, self.checkThread)
        else:
            print("sensor thread done")

    ###
    # Name: textToAudio(self, text)
    # Purpose: Convert a string into audio
    # @input  text (string that will be converted into an mp3 audio file)
    # @return None
    #####    
    def textToAudio(self, text):
        tts = gTTS(text=text, lang='en')	# Convert the text to speech
        audioFile = "audio/question.mp3"	# Save audio as temp file
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
        print("new audio thread created for question")
        # Create an audio thread
        self.audioThread = threading.Thread(target=self.textToAudio, args=(displayPage.currentQuestion_,))
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