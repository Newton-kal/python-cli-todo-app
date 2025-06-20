# todo_app.py

# A Simple Command-Line To-Do List Application 

# This script provides a basic command-line interface for managing a personal
# to-do list. Users can add new tasks, view all tasks, and mark tasks as complete.
# Tasks are saved to a simple text file, ensuring they persist even after the
# application is closed.

# This project demonstrates Python's file handling, list manipulation,
# and basic user interaction.

TODO_FILE = "todos.txt" # Defines the file where our to-do items will be stored

# Helper Functions

def load_tasks():
    """
    Loads tasks from the TODO_FILE. Each line in the file represents a task.
    Tasks are stored as strings in a list.
    Handles cases where the file might not exist yet.
    """
    tasks = []
    try:
        with open(TODO_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip()) # Read each line, remove leading/trailing whitespace
    except FileNotFoundError:
        # If the file doesn't exist, we start with an empty list
        pass
    return tasks

def save_tasks(tasks):
    """
    Saves the current list of tasks back to the TODO_FILE.
    Each task is written on a new line.
    """
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n") # Write each task followed by a new line

def display_tasks(tasks):
    """
    Prints all current tasks to the console with their corresponding number.
    Marks completed tasks (those starting with '[X]').
    """
    if not tasks:
        print("\nYour to-do list is empty. Add some tasks!")
        return

    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks):
        # Enumerate gives us both the index (i) and the item (task)
        # We add 1 to 'i' so the list starts from 1, not 0
        print(f"{i + 1}. {task}")
    print("-----------------------")

# Main Application Logic 

def run_todo_app():
    """
    Manages the main loop and user interaction for the to-do list application.
    """
    tasks = load_tasks() # Load tasks when the app starts

    print("--- Welcome to the Command-Line To-Do App! ---")

    while True:
        print("\nChoose an option:")
        print("1. Add a new task")
        print("2. View tasks")
        print("3. Mark task as complete")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the new task: ")
            tasks.append(task)
            save_tasks(tasks) # Save immediately after adding
            print(f"Task '{task}' added.")
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            display_tasks(tasks) # Show tasks so user can pick one to complete
            if tasks: # Only proceed if there are tasks to mark
                try:
                    task_num = int(input("Enter the number of the task to mark as complete: "))
                    if 1 <= task_num <= len(tasks):
                        # Mark the task by adding '[X]' prefix, if not already marked
                        if not tasks[task_num - 1].startswith("[X]"):
                            tasks[task_num - 1] = "[X] " + tasks[task_num - 1]
                            save_tasks(tasks) # Save immediately after marking
                            print(f"Task {task_num} marked as complete.")
                        else:
                            print("Task already marked as complete.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == '4':
            print("Exiting To-Do App. Goodbye!")
            break # Exit the loop
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# --- Entry Point of the Program ---
if __name__ == "__main__":
    run_todo_app()
              
