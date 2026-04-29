def get_average(student):
    grades = [student["spanish"], student["english"], student["social_studies"], student["science"]]
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


def add_student(students):
    print("\n--- Add Student ---")
    full_name = input("Full name: ").strip()
    section = input("Section (e.g. 11B): ").strip()
    spanish = input_valid_grade("Spanish")
    english = input_valid_grade("English")
    social_studies = input_valid_grade("Social Studies")
    science = input_valid_grade("Science")

    student = {
        "full_name": full_name,
        "section": section,
        "spanish": spanish,
        "english": english,
        "social_studies": social_studies,
        "science": science,
    }
    students.append(student)
    print(f"\nStudent '{full_name}' added successfully.")


def view_all_students(students):
    print("\n--- All Students ---")
    if not students:
        print("No students have been added yet.")
        return

    for i, student in enumerate(students, start=1):
        avg = get_average(student)
        print(f"\n  [{i}] {student['full_name']} | Section: {student['section']}")
        print(f"      Spanish: {student['spanish']} | English: {student['english']} | "
              f"Social Studies: {student['social_studies']} | Science: {student['science']}")
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
