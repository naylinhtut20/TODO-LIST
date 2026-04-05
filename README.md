# TODO-LIST

A simple command-line Todo List app made with Python.

## Features

- Add a new task
- Show all tasks
- Mark a task as done
- Delete a task
- Save tasks in a `todo_list.json` file

## Technologies Used

- Python
- JSON file storage

## How It Works

The program stores tasks in a JSON file so your todo list is saved even after you close the app.

Each task has:
- a task name
- a done status (`True` or `False`)

## Project Structure

```bash
TODO_LIST/
│
├── main.py
├── todo_list.json
└── .gitignore
