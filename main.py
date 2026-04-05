import json
import os

def load_tasks(path_file):
    """Load tasks from the JSON file.
    If the file does not exist or contains invalid JSON, return an empty list.
    Also converts old-format task strings into dictionary format.
    """
    if os.path.exists(path_file):
        try:
            with open(path_file, "r") as file:
                data = json.load(file)

                if not isinstance(data, list):
                    return []

                fixed_tasks = []
                for item in data:
                    if isinstance(item, dict) and "task" in item and "done" in item:
                        fixed_tasks.append(item)
                    elif isinstance(item, str):
                        fixed_tasks.append({"task": item, "done": False})

                return fixed_tasks

        except json.JSONDecodeError:
            return []
    return []

def save_tasks(tasks, path_file):
    """Save all current tasks to the JSON file."""
    with open(path_file, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, path_file):
    """Accept task and save to JSON file."""
    task = input("Enter a task: ")
    tasks.append({"task" : task, "done": False})
    save_tasks(tasks, path_file)
    print("Task added.")

def user_selection(text):
    """Ask to select the task and return selction."""
    try:
        select_task = int(input(f"Enter a task number to {text}: ")) - 1
        return select_task
    except ValueError:
        return -1

def mark_task_complete(tasks, path_file):
    """Change task status as done and save the update list."""
    index = user_selection("mark as done")
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks, path_file)
        print("Marked as done.")
    else:
        print("Invalid task number.")

def delete_task(tasks, path_file):
    """Remove select task from JSON file and save the update list."""
    index = user_selection("remove")
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print(f"Task {index + 1} was removed.")
        save_tasks(tasks, path_file)
    else:
        print("Invalid task number.")

def display_tasks(tasks):
    """Print all tasks in numbered list."""
    if not tasks:
        print("No tasks yet.")
        return

    for i, task in enumerate(tasks, start=1):
        if isinstance(task, dict):
            status = "Done" if task.get("done", False) else "Not done"
            print(f"{i}. {task.get('task', 'Unknown task')} - {status}")
        else:
            print(f"{i}. {task} - Not done")

def print_menu():
    """Display the main MENU"""
    print("1. Add task.")
    print("2. To mark task complete.")
    print("3. Delete task.")
    print("q. Quit.")

def main():
    path_file = "todo_list.json"
    while True:
        tasks = load_tasks(path_file)
        display_tasks(tasks)

        print("______________")
        print_menu()
        choice = input(": ")

        match choice:
            case "1":
                add_task(tasks, path_file)
            case "2":
                mark_task_complete(tasks, path_file)
            case "3":
                delete_task(tasks, path_file)
            case "q"|"quit"|"exit":
                return False
            case _:
                print("Please enter a valid number.")

if __name__ == "__main__":
    main()
    
    