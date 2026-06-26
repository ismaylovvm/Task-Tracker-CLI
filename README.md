# Task Tracker CLI

A lightweight, purely Python-based Command Line Interface (CLI) application to track and manage your daily tasks. 

This project demonstrates foundational software engineering concepts including data persistence, routing, CRUD operations, and Object-Oriented principles using Python dictionaries and JSON serialization. It was built without any external libraries or frameworks.

## 🚀 Features

* **Add Tasks:** Quickly add new tasks to your tracker.
* **Update Tasks:** Modify the description of existing tasks.
* **Delete Tasks:** Remove tasks you no longer need.
* **Change Status:** Mark tasks as `todo`, `in-progress`, or `done`.
* **List & Filter:** View all your tasks or filter them based on their current status.
* **Data Persistence:** All tasks are automatically saved and read from a local `tasks.json` file.

## 🛠️ Technologies Used

* **Python 3** (Core Language)
* **Built-in Modules:** `sys` (argument parsing), `json` (data serialization), `os` (file path validation), `datetime` (time-stamping).

## 📂 File Structure

* `task_cli.py`: The main entry point of the application. Handles user inputs, routing, and task manipulation logic.
* `file_operations.py`: A utility module dedicated to File I/O operations, safely reading from and writing to the JSON database.
* `tasks.json`: The automatically generated database file where tasks are stored as JSON arrays.

## 💻 Usage & Commands

Run the application through your terminal using the following commands:

**1. Adding a new task**
> python task_cli.py add "Buy groceries"

**2. Listing tasks**
> python task_cli.py list
> python task_cli.py list done
> python task_cli.py list todo
> python task_cli.py list in-progress

**3. Updating a task description**
> python task_cli.py update 1 "Buy groceries and cook dinner"

**4. Changing a task's status**
> python task_cli.py mark-in-progress 1
> python task_cli.py mark-done 1

**5. Deleting a task**
> python task_cli.py delete 1

## 🏗️ Data Structure

Tasks are stored in the JSON file using the following schema:

{
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2026-06-25 14:30:00",
    "updatedAt": "2026-06-25 14:30:00"
}

