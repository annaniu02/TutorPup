'''
Filename: database.py
Student: Anna Niu, Yuancheng 'Kaleo' Cao, Tracy Truong
Email: afniu@ucsd.edu, yuc094@ucsd.edu, trtruong@ucsd.edu
Final Project: TutorPup

Description: This file initializes the question and answer database for the
TutorPup application. It contains functinos to add, remove, get, and reset items.
The database uses a list structure.
'''

# Define the list
shared_list = []

###
# Name: add_item(item)
# Purpose: This function will add an entry to the database. An entry consists of
#          the user-inputted question, answer choices, correct answer, and question status.
# @input: item (The entry to be added to the database)
# @return: None
###
def add_item(item):
    shared_list.append(item)

###
# Name: remove_item(item)
# Purpose: This function will remove an entry from the database.
# @input: item (The entry to be deleted from the database)
# @return: None
###
def remove_item(item):
    if item in shared_list:
        shared_list.remove(item)

###
# Name: get_list()
# Purpose: This function will get the entire database.
# @input: None
# @return: The database
###
def get_list():
    return shared_list

###
# Name: reset_database()
# Purpose: This function will reset the database.
# @input: None
# @return: None
###
def reset_database():
    global shared_list
    shared_list = []
