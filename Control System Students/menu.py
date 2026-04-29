from actions import add_student, view_all_students, view_top_3, view_overall_average
from data import export_to_csv, import_from_csv

MENU_OPTIONS = {
    "1": "Add student",
    "2": "View all students",
    "3": "View top 3 students",
    "4": "View overall average",
    "5": "Export data to CSV",
    "6": "Import data from CSV",
    "7": "Exit",
}


def display_menu():
    print("\n========== Student Control System ==========")
    for key, description in MENU_OPTIONS.items():
        print(f"  {key}. {description}")
    print("=============================================")


def get_valid_option():
    while True:
        choice = input("Select an option: ").strip()
        if choice in MENU_OPTIONS:
            return choice
        print(f"Invalid option. Please enter a number between 1 and {len(MENU_OPTIONS)}.")


def run_menu(students):
    while True:
        display_menu()
        choice = get_valid_option()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all_students(students)
        elif choice == "3":
            view_top_3(students)
        elif choice == "4":
            view_overall_average(students)
        elif choice == "5":
            export_to_csv(students)
        elif choice == "6":
            imported = import_from_csv()
            if imported is not None:
                students.clear()
                students.extend(imported)
        elif choice == "7":
            print("\nGoodbye!")
            break
