# MINI PROJECT 3 - TO-DO LIST MANAGEMENT

## 1. Project Description

This is a Python console application for managing a personal to-do list,
built using procedural programming methods.

The program runs on a CLI (Command Line Interface) environment, allowing users
to interact directly through a menu in the console window. The system supports
managing a task list, including features such as adding tasks, displaying the list,
searching, sorting, calculating statistics, saving data, and exporting reports.

This project was developed to apply knowledge from **Programming Methods 1**, including:

- Using functions to break down the program into smaller parts
- Using loops to build an interactive menu
- Using conditional structures to handle user choices
- Using lists and dictionaries to manage data
- Validating input data
- Reading, writing, and exporting data to files
- Presenting data in a formatted table

**Selected Topic:** Topic 6 - Task / To-Do List Management

---

## 2. Project Objective

The system is built with the following main objectives:

- Help users manage a personal task list simply and effectively
- Allow adding, viewing, searching, sorting, and filtering tasks
- Support statistics on task completion status and priority levels
- Save data for reuse in subsequent program runs
- Export structured data to JSON file
- Practice procedural programming thinking and organizing programs into separate functions

---

## 3. Data Structure

Each task is stored as a dictionary with the following fields:

    {
        "id": "T001",
        "title": "Study Python",
        "description": "Review chapter 3 exercises",
        "status": "Pending",
        "priority": 3
    }

The task list is stored in a Python list:

    tasks = [
        {
            "id": "T001",
            "title": "Study Python",
            "description": "Review chapter 3 exercises",
            "status": "Pending",
            "priority": 3
        },
        {
            "id": "T002",
            "title": "Do homework",
            "description": "Submit before deadline",
            "status": "Done",
            "priority": 5
        }
    ]

This structure makes it easy to add, search, sort, and calculate statistics on the data.

---

## 4. Technologies Used

| Component | Role |
|-----------|------|
| Python 3 | Main programming language |
| TXT File (`.txt`) | Persistent data storage and loading |
| JSON File (`.json`) | Structured data export |
| Git & GitHub | Version control |
| CLI | Command line interface for user interaction |

No external libraries are required. The program uses only built-in Python modules (`os`, `json`).

---

## 5. Project Structure

    MINI-PROJECT3-TODO-LIST-APP/
    |-- app.py
    |-- tasks.txt
    |-- tasks.json
    |-- README.md

| File | Function |
|------|----------|
| `app.py` | Main source code file of the program |
| `tasks.txt` | Stores task data in plain text format |
| `tasks.json` | Stores task data in structured JSON format |
| `README.md` | Project description, run instructions, and self-assessment |

---

## 6. Main Features

### 6.1. Add a New Task
Users can enter information for a new task including:
- Task ID
- Title
- Description
- Status (Pending / Done)
- Priority (1–5)

The program validates input to prevent errors such as duplicate IDs, empty fields, or invalid priority values.

### 6.2. Display All Tasks
Displays all tasks in a formatted, aligned table with borders. Columns include ID, Title, Description, Status, and Priority.

### 6.3. Search Task by ID
Users can search for a specific task using its exact ID (case-insensitive). If found, the full task details are displayed.

### 6.4. Sort Tasks by Title
Sorts the entire task list alphabetically by title (A–Z), making it easier to browse when the list is long.

### 6.5. Show Statistics
The program calculates and displays:
- Total number of tasks
- Number of completed tasks (Done)
- Number of pending tasks (Pending)
- Average priority score

### 6.6. Save Tasks to TXT File
Saves the current task list to `tasks.txt`. Data is automatically loaded from this file when the program starts.

### 6.7. Load Tasks from TXT File
Loads task data from `tasks.txt` to restore the previous session's data.

### 6.8. Search Tasks by Keyword
Users can enter a partial keyword to search across task titles (substring match). All matching tasks are displayed in a table.

### 6.9. Export Tasks to JSON
Exports the full task list to `tasks.json` in a structured JSON format, supporting the Advanced Storage requirement.

---

## 7. Menu

When the program runs, the following menu is displayed:

    ============================================================
                    TO-DO LIST MANAGEMENT
    ============================================================
    1. Add a new task
    2. Display all tasks
    3. Search task by ID
    4. Sort tasks by title
    5. Show statistics
    6. Save tasks to TXT file
    7. Load tasks from TXT file
    8. Search tasks by keyword
    9. Export tasks to JSON
    0. Exit
    ============================================================

Users enter a number from 0 to 9 to select the corresponding feature. If an invalid choice is entered, the program displays an error message and prompts again without crashing.

---

## 8. Input Validation

The program validates input for important fields:

| Data | Validation Rule |
|------|----------------|
| Task ID | Cannot be empty |
| Task ID | Cannot be duplicate |
| Task Title | Cannot be empty |
| Status | Must be `Pending` or `Done` |
| Priority | Must be an integer from 1 to 5 |

---

## 9. Main Functions in the Program

The program is divided into small functions following Top-Down design and Single Responsibility principles:

| Function | Role |
|----------|------|
| `display_menu()` | Display the main menu |
| `load_from_txt()` | Load task data from TXT file |
| `save_to_txt()` | Save task data to TXT file |
| `export_to_json()` | Export task data to JSON file |
| `add_task()` | Add a new task |
| `display_tasks()` | Display all tasks in table format |
| `search_task_by_id()` | Search task by exact ID |
| `sort_tasks_by_title()` | Sort tasks alphabetically by title |
| `show_statistics()` | Calculate and display task statistics |
| `search_tasks_by_keyword()` | Search tasks by keyword (substring) |
| `is_duplicate_id()` | Check for duplicate task ID |
| `input_status()` | Validate status input |
| `input_priority()` | Validate priority input |
| `main()` | Control the main program flow |

---

## 10. Usage Examples

### 10.1. Adding a Task

    Enter task ID: T001
    Enter task title: Study Python
    Enter description: Review chapter 3 exercises
    Enter status (Pending/Done): Pending
    Enter priority (1-5): 3
    => Task added successfully.

### 10.2. Displaying All Tasks

    +----------+----------------------+---------------------------+------------+----------+
    | ID       | Title                | Description               | Status     | Priority |
    +----------+----------------------+---------------------------+------------+----------+
    | T001     | Study Python         | Review chapter 3          | Pending    | 3        |
    | T002     | Do homework          | Submit before deadline    | Done       | 5        |
    +----------+----------------------+---------------------------+------------+----------+

### 10.3. Statistics

    TASK STATISTICS
    Total tasks      : 2
    Completed tasks  : 1
    Pending tasks    : 1
    Average priority : 4.00

---

## 11. Advanced Features Implemented

### 11.1. Keyword Search (Substring Match)
Users can enter a partial keyword to find tasks. For example, entering `Study` will find all tasks with "Study" in the title. This satisfies the **Advanced Search & Filter** requirement.

### 11.2. JSON Export
The program exports all task data to a structured `tasks.json` file. This satisfies the **Advanced Storage – JSON** requirement.

---

## 12. How to Run

**Requirements:** Python 3.x installed

    python app.py

No installation of external libraries is needed.

---

## 13. Self-Assessment (Tự chấm điểm)

| # | Component | Criteria | Max | Score |
|---|-----------|----------|-----|-------|
| 1 | CLI Menu System | Interactive menu with `while True` loop; handles invalid input without crashing | 1.0 | 1.0 |
| 2 | Data Input & Validation | Validates duplicate ID, status (Pending/Done), priority (1–5 integer) | 1.0 | 1.0 |
| 3 | Data Display | All records printed in a formatted, aligned table with borders | 1.0 | 1.0 |
| 4 | Basic Search | Search by exact task ID (case-insensitive) | 1.0 | 1.0 |
| 5 | Sorting Mechanism | Sort tasks alphabetically by title | 1.0 | 1.0 |
| 6 | Basic Calculation | Shows total tasks, completed, pending, and average priority | 1.0 | 1.0 |
| 7 | TXT File Handling | Saves data to `tasks.txt` and loads on startup without data loss | 1.0 | 1.0 |
| 8 | [Advanced] Complex Logic | Substring keyword search across task titles | 1.0 | 1.0 |
| 9 | [Advanced] JSON / DBMS | Export all tasks to structured `tasks.json` file | 1.0 | 1.0 |
| 10 | Git & Modular Code | Hosted on GitHub with ≥ 3 commits; code divided into single-responsibility functions | 1.0 | 1.0 |
| | **TOTAL** | | **10.0** | **10.0** |

---

## 14. Student Information

- **Student Name:** [TRẦN LÊ BẢO NGHI]
- **Student ID:** [24S7040007]
- **Class:** [Tin2E]
- **Course:** Programming Methods 1
- **Instructor:** Dr. Tran Van Long
- **Faculty of Informatics, Hue University of Education**