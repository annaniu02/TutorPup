import json

def read_questions_from_file(filename='database.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def write_questions_to_file(questions, filename='database.json'):
    with open(filename, 'w') as file:
        json.dump(questions, file, indent=4)
