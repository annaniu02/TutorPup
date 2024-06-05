import tkinter as tk
from tkinter import ttk
from supabase_client import supabase 

import home
import help
import question_display

HEADERFONT = ("Verdana", 40)
LARGEFONT =("Verdana", 30)
MEDIUMFONT =("Verdana", 20)
SMALLFONT =("Verdana", 15)
BTNFONT =("Verdana", 35)

# Question Input Page -- where user can add their questions and answers
class inputPage(tk.Frame):
    def __init__(self, parent, controller):

        # Function to add user input question-answers to the database when ADD button is clicked
        def addToDatabase():
            question = q_entry.get()
            answer_a = a_entry.get()
            answer_b = b_entry.get()
            answer_c = c_entry.get()
            correct_answer = correct_entry.get()

            # Clear the entries after getting their values
            q_entry.delete(0, tk.END)
            a_entry.delete(0, tk.END)
            b_entry.delete(0, tk.END)
            c_entry.delete(0, tk.END)
            correct_entry.delete(0, tk.END)

            # Add data to Supabase
            data = {
                "Question": question,
                "option_a": answer_a,
                "option_b": answer_b,
                "option_c": answer_c,
                "correct_answer": correct_answer
            }
            response = supabase.table('question_bank').insert(data).execute()
            print("Response:", response)  # For debugging



        tk.Frame.__init__(self, parent)
        
        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        

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
        helpBtn.grid(row = 0, column = 6, padx = 10, pady = 10, sticky = tk.NE)

        # label of header
        label = ttk.Label(self, text ="Input your question and answer choices below \n"
                          "In the last blank, input the correct answer letter",
                          font = LARGEFONT, background = "#f9cb9c", anchor="center")
        # putting the grid in its place by using grid
        label.grid(row = 0, column = 1, columnspan = 4)

        # Question and answer labels and entry fields
        q_label = ttk.Label(self, text="Q:", font=MEDIUMFONT, background = "#f9cb9c")
        q_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        q_entry = ttk.Entry(self, font=MEDIUMFONT)
        q_entry.grid(row=1, column=1, columnspan=4, padx=10, pady=10, sticky=tk.W+tk.E)

        a_label = ttk.Label(self, text="A:", font=MEDIUMFONT, background = "#f9cb9c")
        a_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        a_entry = ttk.Entry(self, font=MEDIUMFONT)
        a_entry.grid(row=2, column=1, columnspan=4, padx=10, pady=10, sticky=tk.W+tk.E)

        b_label = ttk.Label(self, text="B:", font=MEDIUMFONT, background = "#f9cb9c")
        b_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)
        b_entry = ttk.Entry(self, font=MEDIUMFONT)
        b_entry.grid(row=3, column=1, columnspan=4, padx=10, pady=10, sticky=tk.W+tk.E)

        c_label = ttk.Label(self, text="C:", font=MEDIUMFONT, background = "#f9cb9c")
        c_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.E)
        c_entry = ttk.Entry(self, font=MEDIUMFONT)
        c_entry.grid(row=4, column=1, columnspan=4, padx=10, pady=10, sticky=tk.W+tk.E)

        correct_label = ttk.Label(self, text="Correct\n(A,B,C):", font=MEDIUMFONT, background = "#f9cb9c")
        correct_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.E)
        correct_entry = ttk.Entry(self, font=MEDIUMFONT)
        correct_entry.grid(row=5, column=1, columnspan=4, padx=10, pady=10, sticky=tk.W+tk.E)

        # Place ADD button to add question to question deck
        # TODO: connect this adding question functionality to database
        # TODO: after ADD button clicked, entries should be stored in database and entry text box inputs should be cleared so user can input next questions/answers
        # TODO: do we want screen where user can review questions currently in database?
        addBtn = ttk.Button(self, text ="ADD", style = 'btn.TButton',
                                command = addToDatabase)
        addBtn.grid(row = 6, column = 0, columnspan = 3, rowspan = 1)

        # Place DONE button to move to question display slides
        doneBtn = ttk.Button(self, text ="DONE", style = 'btn.TButton',
                                command = lambda : controller.show_frame(question_display.displayPage))
        doneBtn.grid(row = 6, column = 3, columnspan = 3, rowspan = 1)
