""" To-Do List Program (Console) 

PURPOSE: Provide a simple, text-based To-Do List manager that lets a user add tasks, view all tasks, and mark tasks as completed. 

HOW IT WORKS (high level): - The program keeps an in-memory list called tasks. - Each task is stored as a dictionary with two keys: "description" : str -> what the user needs to do "status" : str -> either "Pending" or "Completed" - A menu is shown repeatedly until the user chooses to exit. - Based on the user's choice, the program calls one of three functions: add_task(), view_tasks(), or complete_task(). 

INPUTS: - Task descriptions typed by the user (strings). - Menu choices typed by the user (strings like "1", "2", "3", "4"). - A task number (integer) when marking a task as completed. 

OUTPUTS: - A neatly formatted list of tasks with their status. - Informational messages confirming actions or explaining errors. 

NOTES / LIMITATIONS: - Data is not saved to a file; when the program ends, tasks are lost. - Empty descriptions are not prevented by default (could be enhanced). - Only "Completed" vs. "Pending" states are tracked (no due dates, etc.).
----------------------------------------------------------------------------- 

DATA MODEL 

----------------------------------------------------------------------------- 

tasks will hold zero or more task "records". 

Each record is a dictionary like: 

{"description": "Buy groceries", "status": "Pending"} 

We use a list to preserve the order that tasks were added. 
"""

tasks = [] 

"""
----------------------------------------------------------------------------- 

UI / MENU 

----------------------------------------------------------------------------- 
"""

def show_menu():
    """ Display the main menu options for the user.
     This function only prints text; it does not read input. 
    """
    print("\n--- TO-DO LIST MENU ---") 
    print("1. Add Task") 
    print("2. View Tasks") 
    print("3. Mark Task as Completed") 
    print("4. Exit") 

"""
----------------------------------------------------------------------------- 

CORE FEATURES 

----------------------------------------------------------------------------- 
"""

def add_task(): """ Ask the user for a task description and add it to the tasks list with a default status of 'Pending'. 

SIDE EFFECTS: 
    - Modifies the global `tasks` list by appending a new dictionary. 
 
USER EXPERIENCE: 
    - Prompts the user for text. 
    - Confirms that the task was added. 
""" 
description = input("Enter task description: ") 
 
# NOTE: We accept any text (including empty strings). 
# If you want to forbid empty descriptions, you could add: 
#   if not description.strip(): 
#       print("Description cannot be empty."); return 
tasks.append({"description": description, "status": "Pending"}) 
print(f'Task "{description}" added successfully!') 
  
def view_tasks(): """ Display all tasks in a numbered list. Shows each task's description and status in the format: 1. Do laundry [Pending] 

EDGE CASE: 
    - If there are no tasks yet, inform the user. 
""" 
if not tasks:  # True when the list is empty 
    print("No tasks available.") 
else: 
    print("\nYour Tasks:") 
    # enumerate(..., start=1) shows human-friendly numbering (1, 2, 3, ...) 
    for i, task in enumerate(tasks, start=1): 
        # Access dictionary values with task['description'] and task['status'] 
        print(f"{i}. {task['description']} [{task['status']}]") 
  
def complete_task(): 
    """ Let the user select a task (by its displayed number) and mark it as completed. 

    PROCESS: 
        1) If there are no tasks, print a message and return early. 
        2) Show the current tasks so the user can see the numbers. 
        3) Ask the user for a task number. 
        4) Convert the input to an integer inside a try/except to catch non-numbers. 
        5) Validate that the number is within range. 
        6) Update the chosen task's status to 'Completed'. 
    
    ERROR HANDLING: 
        - If the input is not an integer (e.g., 'abc'), catch ValueError 
        and print a friendly message. 
        - If the number is outside the valid range, inform the user. 
    """ 
    if not tasks: 
        print("No tasks to complete.") 
        return  # Early exit: nothing to do 
 
# Show tasks so the user can see which number to enter 
view_tasks() 
 
try: 
    user_input = input("Enter task number to mark as completed: ") 
    choice = int(user_input)  # could raise ValueError if not a valid integer 
 
    # Check that the number corresponds to an existing task. 
    # Valid numbers are 1 through len(tasks) (inclusive). 
    if 1 <= choice <= len(tasks): 
        # Convert the human-friendly number (1-based) to the 
        # list index (0-based) by subtracting 1. 
        tasks[choice - 1]["status"] = "Completed" 
        print(f'Task "{tasks[choice - 1]["description"]}" marked as completed!') 
    else: 
        # The user typed a number, but it's not a valid task number. 
        print("Invalid task number. Please choose a number shown in the list.") 
 
except ValueError: 
    # Happens if the user typed something like "three" instead of "3". 
    print("Please enter a valid number (e.g., 1, 2, or 3).") 
  
"""
----------------------------------------------------------------------------- 

MAIN PROGRAM LOOP 

----------------------------------------------------------------------------- 

Thids loop keeps the program running, showing the menu and responding to choices 

until the user selects "4" to exit. 
"""

while True: 
    # Step 1: display options every cycle 
    show_menu() 
    # Step 2: read user decision 
    choice = input("Enter your choice (1-4): ") 

    # Step 3: route to the appropriate action 
    if choice == "1": 
        # ADD a new task 
        add_task() 
    elif choice == "2": 
        # VIEW all tasks 
        view_tasks() 
    elif choice == "3": 
        # MARK a task as completed 
        complete_task() 
    elif choice == "4": 
        # EXIT the program: break stops the infinite loop 
        print("Goodbye! Thanks for using the To-Do List.") 
        break 
    else: 
        # Any other input is not a valid menu option 
        print("Invalid option. Please choose 1, 2, 3, or 4.") 
