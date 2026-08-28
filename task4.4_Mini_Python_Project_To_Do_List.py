# ============================================================
# Mini Python Project: To-Do List
# Concepts: Variables, Data Types, Input/Output, Conditions,
# Loops, Functions, Data Structures, File Handling,
# Exception Handling, and Python Libraries
# ============================================================

import json
from datetime import datetime

# File used to store tasks
FILE_NAME = "todo_tasks.json"


# ------------------------------------------------------------
# Function 1: Load tasks from file
# ------------------------------------------------------------
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: Task file contains invalid data.")
        return []


# ------------------------------------------------------------
# Function 2: Save tasks to file
# ------------------------------------------------------------
def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)

    except IOError:
        print("Error: Unable to save tasks.")


# ------------------------------------------------------------
# Function 3: Add a new task
# ------------------------------------------------------------
def add_task(tasks):
    task_name = input("Enter the task: ").strip()

    if task_name == "":
        print("Error: Task cannot be empty.")
        return

    task = {
        "title": task_name,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


# ------------------------------------------------------------
# Function 4: Display all tasks
# ------------------------------------------------------------
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n========== TO-DO LIST ==========")

    for index, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(f"{index}. {task['title']}")
        print(f"   Status: {status}")
        print(f"   Created: {task['created_at']}")

    print("================================")


# ------------------------------------------------------------
# Function 5: Mark task as completed
# ------------------------------------------------------------
def complete_task(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to mark as completed: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)

            print("Task marked as completed!")

        else:
            print("Error: Invalid task number.")

    except ValueError:
        print("Error: Please enter a valid number.")


# ------------------------------------------------------------
# Function 6: Delete a task
# ------------------------------------------------------------
def delete_task(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)

            print(f"Task '{removed_task['title']}' deleted successfully!")

        else:
            print("Error: Invalid task number.")

    except ValueError:
        print("Error: Please enter a valid number.")


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------
def main():
    tasks = load_tasks()

    while True:

        print("\n========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Thank you for using the To-Do List!")
            break

        else:
            print("Error: Invalid choice. Please select 1-5.")


# Start the program
if __name__ == "__main__":
    main()