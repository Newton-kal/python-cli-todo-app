# Simple Command-Line To-Do List

A straightforward command-line application built in Python that allows users to manage a personal to-do list. This project demonstrates core programming concepts including user interaction, list manipulation, and file handling for data persistence.

---

## Features

* **Add Tasks:** Add new items to your to-do list.
* **View Tasks:** Display all current tasks with sequential numbering.
* **Mark as Complete:** Mark tasks as completed, indicated by an `[X]` prefix.
* **Data Persistence:** Tasks are saved to a `todos.txt` file, so they are remembered even after closing and reopening the application.

---

## Technologies Used

* Python 3.x

---

## How to Run

1.  **Clone the repository (if you're running it locally):**
    ```bash
    git clone [https://github.com/Newton-Kal/python-cli-todo-app.git](https://github.com/Newton-Kal/python-cli-todo-app.git)
    cd python-cli-todo-app
    ```

2.  **Run the application:**
    ```bash
    python todo_app.py
    ```

---

## Example Usage


   --- Welcome to the Command-Line To-Do App! ---
   Choose an option:
   * Add a new task
   * View tasks
   * Mark task as complete
   * Exit
     Enter your choice (1-4): 1
     Enter the new task: Learn Git basics
     Task 'Learn Git basics' added.
   Choose an option:
   * Add a new task
   * View tasks
   * Mark task as complete
   * Exit
     Enter your choice (1-4): 1
     Enter the new task: Complete Python project
     Task 'Complete Python project' added.
   Choose an option:
   * Add a new task
   * View tasks
   * Mark task as complete
   * Exit
     Enter your choice (1-4): 2
   --- Your To-Do List ---
   * Learn Git basics
   * Complete Python project
   Choose an option:
   * Add a new task
   * View tasks
   * Mark task as complete
   * Exit
     Enter your choice (1-4): 3
   --- Your To-Do List ---
   * Learn Git basics
   * Complete Python project
   Enter the number of the task to mark as complete: 1
   Task 1 marked as complete.
   Choose an option:
   * Add a new task
   * View tasks
   * Mark task as complete
   * Exit
     Enter your choice (1-4): 2
   --- Your To-Do List ---
   * [X] Learn Git basics
   * Complete Python project
   Choose an option:
   * Add a new task
   * View tasks
   * Mark task as complete
   * Exit
     Enter your choice (1-4): 4
     Exiting To-Do App. Goodbye!
   
---

## Future Enhancements (Ideas for continued development)

* Add functionality to delete tasks.
* Implement an "undo" feature for marking tasks complete.
* Allow users to edit existing tasks.
* Categorize tasks (e.g., Work, Personal).
* Add due dates to tasks.
