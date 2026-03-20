import csv


def read_csv_file(file_path):
  with open(r"C:\Users\Paulo\Documents\Lyfter\Python\Managing_archives\\ejemplo.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      print(row)

read_csv_file('ejemplo.csv')