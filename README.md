# MINI PROJECT 3 - TO-DO LIST MANAGEMENT

## 1. Project Description

This project is a Python console application for managing a personal to-do list.
The program allows users to add, display, search, sort, save, and load tasks.
It was developed for **Mini Project 3 - Procedural Programming Application** in **Programming Methods 1**.

**Selected Topic:** Topic 6 - Task / To-Do List Management

---

## 2. Project Objective

The objective of this project is to apply procedural programming concepts such as:
- Functions
- Loops
- Conditionals
- Input validation
- File handling (TXT)
- JSON export

The system is designed to run in a CLI (Command Line Interface) environment.

---

## 3. Main Features

The application supports the following functions:

1. Add a new task
2. Display all tasks in table format
3. Search task by ID
4. Sort tasks by title
5. Show task statistics
6. Save tasks to TXT file
7. Load tasks from TXT file
8. Search tasks by keyword (substring match)
9. Export tasks to JSON
0. Exit program

---

## 4. Technologies Used

- Python 3
- Text File (`.txt`) — for persistent data storage
- JSON File (`.json`) — for structured data export
- Git & GitHub — for version control

---

## 5. Project Structure

    MINI-PROJECT3-TODO-LIST-APP/
    |-- app.py
    |-- tasks.txt
    |-- tasks.json
    |-- README.md

---

## 6. How to Run

**Requirements:** Python 3.x installed

    python app.py

No external libraries are required. The program uses only built-in Python modules (`os`, `json`).

---

## 7. Self-Assessment (Tự chấm điểm)

| # | Component | Criteria | Score |
|---|-----------|----------|-------|
| 1 | CLI Menu System | Interactive menu with `while True` loop; handles invalid input without crashing | 1.0 / 1.0 |
| 2 | Data Input & Validation | Validates duplicate ID, status (Pending/Done), priority (1–5 integer) | 1.0 / 1.0 |
| 3 | Data Display | All records printed in a formatted, aligned table with borders | 1.0 / 1.0 |
| 4 | Basic Search | Search by exact task ID (case-insensitive) | 1.0 / 1.0 |
| 5 | Sorting Mechanism | Sort tasks alphabetically by title | 1.0 / 1.0 |
| 6 | Basic Calculation | Shows total tasks, completed, pending, and average priority | 1.0 / 1.0 |
| 7 | TXT File Handling | Saves data to `tasks.txt` and loads on startup without data loss | 1.0 / 1.0 |
| 8 | [Advanced] Complex Logic | Substring keyword search across task titles | 1.0 / 1.0 |
| 9 | [Advanced] JSON / DBMS | Export all tasks to structured `tasks.json` file | 1.0 / 1.0 |
| 10 | Git & Modular Code | Hosted on GitHub with ≥ 3 commits; code divided into single-responsibility functions | 1.0 / 1.0 |
| | **TOTAL** | | **10.0 / 10.0** |

---

