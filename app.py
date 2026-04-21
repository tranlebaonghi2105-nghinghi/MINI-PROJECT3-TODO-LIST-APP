import os
import json

TXT_FILE = "tasks.txt"
JSON_FILE = "tasks.json"


def display_menu():
    print("\n" + "=" * 50)
    print("        TO-DO LIST MANAGEMENT")
    print("=" * 50)
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
    print("=" * 50)


def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Feature 1 is under development.")
        elif choice == "2":
            print("Feature 2 is under development.")
        elif choice == "3":
            print("Feature 3 is under development.")
        elif choice == "4":
            print("Feature 4 is under development.")
        elif choice == "5":
            print("Feature 5 is under development.")
        elif choice == "6":
            print("Feature 6 is under development.")
        elif choice == "7":
            print("Feature 7 is under development.")
        elif choice == "8":
            print("Feature 8 is under development.")
        elif choice == "9":
            print("Feature 9 is under development.")
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 9.")


if __name__ == "__main__":
    main()