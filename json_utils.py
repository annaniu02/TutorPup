'''
Filename: json_utils.py
Student: Anna Niu, Yuancheng 'Kaleo' Cao, Tracy Truong
Email: afniu@ucsd.edu, yuc094@ucsd.edu, trtruong@ucsd.edu
Final Project: TutorPup

Description: This file was originally where the database elements are accessed.
THIS FILE IS NO LONGER USED IN THE FINAL VERSION OF THE TutorPup APPLICATION.
'''

import json

###
# Name: read_questions_from_file(filename='database.json')
# Purpose: Reads question and answer content from database.json
# @input  filename (The database.json file)
# @return The content in database
####  
def read_questions_from_file(filename='database.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
###
# Name: write_questions_to_file(questions, filename='database.json')
# Purpose: Writes question and answer content to database.json
# @input  questions (The questions to be written to the database file),
#         filename (The database.json file)
# @return None
####  
def write_questions_to_file(questions, filename='database.json'):
    with open(filename, 'w') as file:
        json.dump(questions, file, indent=4)
