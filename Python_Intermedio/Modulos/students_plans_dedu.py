import csv
import os

# Duplique el proyecto Sistema control de Estudiantes y modifíquelo para usar objetos para 
# guardar la información de los estudiantes (creando una clase de Student).
# Hay que cambiar los estudiantes de diccionarios a objetos.
# Hay que convertir la data del csv 
# (que viene por defecto en formato de diccionario) a objetos al importarla.
# Hay que convertir los objetos a diccionarios para poder exportarlos a csv.
# Hay que modificar el acceso a los keys para accesar a atributos.
# student[’Name’] → student.name

# ==================== CONSTANTES ====================

CSV_FILENAME = "students.csv"
CSV_HEADERS = ["full_name", "section", "spanish", "english", "social_studies", "science"]

MENU_OPTIONS = {
    "1": "Add student",
    "2": "View all students",
    "3": "View top 3 students",
    "4": "View overall average",
    "5": "Export data to CSV",
    "6": "Import data from CSV",
    "7": "Exit",
}


# ==================== ACCIONES ====================

def get_average(student):
    grades = [ student.english, student.social_studies, student.science, student.spanish]
    return sum(grades) / len(grades)


def input_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"  {subject} grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("  Invalid grade. Please enter a number between 0 and 100.")
        except ValueError:
            print("  Invalid input. Please enter a numeric value.")



class Student():
    def __init__(self, full_name, section,spanish,english,social_studies,science):
        self.full_name = full_name
        self.section= section
        self.spanish = spanish
        self.english= english
        self.social_studies= social_studies
        self.science=science


def add_student(students):
    full_name= input("Añadir su nombre completo: ")
    section= input("Añadir su seccion:")
    spanish= int(input("Añadir su nota de español: "))
    english= int(input("Añadir su nota de english: "))
    social_studies= int(input("Añadir su nota de social_studies:"))
    science= int(input("Añadir su nota de science: "))
    student_1 = Student(full_name, section,spanish,english,social_studies,science)
    students.append(student_1)



def view_all_students(students):
    print("\n--- All Students ---")
    if not students:
        print("No students have been added yet.")
        return

    for i, student in enumerate(students, start=1):
        avg = get_average(student)
        print(f"\n  [{i}] Name {student.full_name} | Section:{student.section}")
        print(f"      Spanish: {student.spanish} | English: {student.english} | "
              f"Social Studies: {student.social_studies} | Science: {student.science}")
        print(f"      Average: {avg:.2f}")


def view_top_3(students):
    print("\n--- Top 3 Students by Average ---")
    if not students:
        print("No students have been added yet.")
        return

    sorted_students = sorted(students, key=get_average, reverse=True)
    top = sorted_students[:3]

    for rank, student in enumerate(top, start=1):
        avg = get_average(student)
        print(f"  #{rank} {student['full_name']} | Section: {student['section']} | Average: {avg:.2f}")


def view_overall_average(students):
    print("\n--- Overall Average ---")
    if not students:
        print("No students have been added yet.")
        return

    total = sum(get_average(student) for student in students)
    overall = total / len(students)
    print(f"  Overall average across all {len(students)} student(s): {overall:.2f}")


# ==================== DATOS (CSV) ====================

def export_to_csv(students):
    with open(CSV_FILENAME, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_HEADERS)
        writer.writeheader()
        writer.writerows(students)
    print(f"\nData exported successfully to '{CSV_FILENAME}'.")


def import_from_csv():
    if not os.path.exists(CSV_FILENAME):
        print("\nNo exported file found. Please export data first.")
        return None

    students = []
    with open(CSV_FILENAME, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({
                "full_name": row["full_name"],
                "section": row["section"],
                "spanish": float(row["spanish"]),
                "english": float(row["english"]),
                "social_studies": float(row["social_studies"]),
                "science": float(row["science"]),
            })

    print(f"\nData imported successfully from '{CSV_FILENAME}'. {len(students)} student(s) loaded.")
    return students


# ==================== MENÚ ====================

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


# ==================== PROGRAMA PRINCIPAL ====================

def main():
    students = []
    run_menu(students)


if __name__ == "__main__":
    main()