import os
import json

TXT_FILE = "tasks.txt"
JSON_FILE = "tasks.json"


def clear_screen():
    os.system("cls")


def display_menu():
    clear_screen()
    print("\n" + "=" * 60)
    print("                TO-DO LIST MANAGEMENT")
    print("=" * 60)
    print("1. Add a new task")
    print("2. Display all tasks")
    print("3. Search task by ID")
    print("4. Sort tasks by title")
    print("5. Show statistics")
    print("6. Save tasks to TXT file")
    print("7. Load tasks from TXT file")
    print("8. Search tasks by keyword")
    print("9. Export tasks to JSON")
    print("0. Exit")
    print("=" * 60)


def is_duplicate_id(tasks, task_id):
    for task in tasks:
        if task["id"].lower() == task_id.lower():
            return True
    return False


def input_status():
    while True:
        status = input("Enter status (Pending/Done): ").strip().lower()
        if status in ["pending", "done"]:
            return status.capitalize()
        print("Invalid status. Please enter Pending or Done.")


def input_priority():
    while True:
        priority = input("Enter priority (1-5): ").strip()
        if priority.isdigit():
            priority = int(priority)
            if 1 <= priority <= 5:
                return priority
        print("Invalid priority. Please enter a number from 1 to 5.")


def add_task(tasks):
    print("\nADD NEW TASK")

    while True:
        task_id = input("Enter task ID: ").strip()
        if task_id == "":
            print("Task ID cannot be empty.")
        elif is_duplicate_id(tasks, task_id):
            print("Task ID already exists.")
        else:
            break

    while True:
        title = input("Enter task title: ").strip()
        if title == "":
            print("Task title cannot be empty.")
        else:
            break

    description = input("Enter description: ").strip()
    status = input_status()
    priority = input_priority()

    new_task = {
        "id": task_id,
        "title": title,
        "description": description,
        "status": status,
        "priority": priority
    }

    tasks.append(new_task)
    print("Task added successfully.")


def display_tasks(tasks):
    if not tasks:
        print("Task list is empty.")
        return

    id_width = 8
    title_width = 20
    description_width = 25
    status_width = 10
    priority_width = 8

    border = (
        "+"
        + "-" * (id_width + 2)
        + "+"
        + "-" * (title_width + 2)
        + "+"
        + "-" * (description_width + 2)
        + "+"
        + "-" * (status_width + 2)
        + "+"
        + "-" * (priority_width + 2)
        + "+"
    )

    print("\n" + border)
    print(
        f"| {'ID':<{id_width}} "
        f"| {'Title':<{title_width}} "
        f"| {'Description':<{description_width}} "
        f"| {'Status':<{status_width}} "
        f"| {'Priority':<{priority_width}} |"
    )
    print(border)

    for task in tasks:
        print(
            f"| {task['id'][:id_width]:<{id_width}} "
            f"| {task['title'][:title_width]:<{title_width}} "
            f"| {task['description'][:description_width]:<{description_width}} "
            f"| {task['status'][:status_width]:<{status_width}} "
            f"| {str(task['priority'])[:priority_width]:<{priority_width}} |"
        )

    print(border)


def search_task_by_id(tasks):
    if not tasks:
        print("Task list is empty.")
        return

    task_id = input("Enter task ID to search: ").strip()

    for task in tasks:
        if task["id"].lower() == task_id.lower():
            print("\nTask found:")
            print(f"ID         : {task['id']}")
            print(f"Title      : {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Status     : {task['status']}")
            print(f"Priority   : {task['priority']}")
            return

    print("Task not found.")


def sort_tasks_by_title(tasks):
    if not tasks:
        print("Task list is empty.")
        return

    tasks.sort(key=lambda task: task["title"].lower())
    print("Tasks sorted by title successfully.")


def show_statistics(tasks):
    if not tasks:
        print("Task list is empty.")
        return

    total_tasks = len(tasks)
    done_tasks = 0
    pending_tasks = 0
    total_priority = 0

    for task in tasks:
        if task["status"] == "Done":
            done_tasks += 1
        else:
            pending_tasks += 1
        total_priority += task["priority"]

    average_priority = total_priority / total_tasks

    print("\nTASK STATISTICS")
    print(f"Total tasks      : {total_tasks}")
    print(f"Completed tasks  : {done_tasks}")
    print(f"Pending tasks    : {pending_tasks}")
    print(f"Average priority : {average_priority:.2f}")


def save_to_txt(tasks, filename=TXT_FILE):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for task in tasks:
                line = (
                    f"{task['id']}|{task['title']}|{task['description']}|"
                    f"{task['status']}|{task['priority']}\n"
                )
                file.write(line)
        print(f"Tasks saved to {filename} successfully.")
    except Exception as e:
        print(f"Error while saving file: {e}")


def load_from_txt(filename=TXT_FILE):
    tasks = []

    if not os.path.exists(filename):
        return tasks

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 5:
                    task = {
                        "id": parts[0],
                        "title": parts[1],
                        "description": parts[2],
                        "status": parts[3],
                        "priority": int(parts[4])
                    }
                    tasks.append(task)
    except Exception as e:
        print(f"Error while loading file: {e}")

    return tasks


def search_tasks_by_keyword(tasks):
    if not tasks:
        print("Task list is empty.")
        return

    keyword = input("Enter keyword to search in title: ").strip().lower()
    found_tasks = []

    for task in tasks:
        if keyword in task["title"].lower():
            found_tasks.append(task)

    if found_tasks:
        display_tasks(found_tasks)
    else:
        print("No tasks found with that keyword.")


def export_to_json(tasks, filename=JSON_FILE):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)
        print(f"Tasks exported to {filename} successfully.")
    except Exception as e:
        print(f"Error while exporting JSON: {e}")


def main():
    tasks = load_from_txt()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            search_task_by_id(tasks)
        elif choice == "4":
            sort_tasks_by_title(tasks)
        elif choice == "5":
            show_statistics(tasks)
        elif choice == "6":
            save_to_txt(tasks)
        elif choice == "7":
            tasks = load_from_txt()
            print("Tasks loaded successfully.")
        elif choice == "8":
            search_tasks_by_keyword(tasks)
        elif choice == "9":
            export_to_json(tasks)
        elif choice == "0":
            save_to_txt(tasks)
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 9.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()