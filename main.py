import json
import os

path_file = "todo_list.json"

def load_tasks():
    """Load tasks from thee JSON file if exists.
    if the file does not exist or contains invalid JSON, start with an empty list.
    """
    if os.path.exists(path_file):
        try:
            with open(path_file, "r") as file:
                return json.load(file)
        except:
            return []
    return []

tasks = load_tasks()

def save_tasks(tasks):
    """Save all current tasks to the JSON file."""
    with open(path_file, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    """Accept task and save to JSON file."""
    task = input("Enter a task: ")
    tasks.append({"task" : task, "done": False})
    save_tasks(tasks)
    print("Task added.")

def user_selection(text):
    """Ask to select the task and return selction."""
    try:
        select_task = int(input(f"Enter a tesk number to {text}: ")) - 1
        return select_task
    except ValueError:
        return -1

def mark_task_complete():
    """Change task status as done and save the update list."""
    index = user_selection("mark as done")
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Marked as done.")
    else:
        print("Invalid task number.")

def delete_task():
    """Remove select task from JSON file and save the update list."""
    index = user_selection("remove")
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print(f"Task {index + 1} was removed.")
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def display_tasks():
    """Print all tasks in numbered list."""
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not done"
        print(f"{i}. {task['task']} - {status}")

def print_menu():
    """Display the main MENU"""
    print("1. Add task.")
    print("2. To mark task complete.")
    print("3. Delete task.")
    print("q. Quit.")

def main():
    while True:
        display_tasks()
        print("______________")
        print_menu()
        index = input(": ")
        match index:
            case "1":
                add_task()
            case "2":
                mark_task_complete()
            case "3":
                delete_task()
            case "q"|"quit"|"exit":
                return False
            case _:
                print("Please enter a valid number.")

if __name__ == "__main__":
    main()
    
    