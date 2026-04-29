import csv
import os

CSV_FILENAME = "students.csv"
CSV_HEADERS = ["full_name", "section", "spanish", "english", "social_studies", "science"]


def export_to_csv(students):
    with open(CSV_FILENAME, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_HEADERS)
        writer.writeheader()
        writer.writerows(students)
    print(f"\nData exported successfully to '{CSV_FILENAME}'.")


def import_from_csv():
    if not os.path.exists(CSV_FILENAME):
        print(f"\nNo exported file found. Please export data first.")
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
