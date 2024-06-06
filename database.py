# Define the list
shared_list = []

# Function to add an item to the list
def add_item(item):
    shared_list.append(item)

# Function to remove an item from the list
def remove_item(item):
    if item in shared_list:
        shared_list.remove(item)

# Function to get the list
def get_list():
    return shared_list

def reset_database():
    global shared_list
    shared_list = []
