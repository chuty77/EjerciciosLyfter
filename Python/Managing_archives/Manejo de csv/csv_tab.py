import csv

def input_videogames():
    while True:
        try:
            n = int(input("¿How many games do you wanto to register? "))
            if n > 0:
                break
            else:
                print("Please enter a number higher than 0.")
        except ValueError:
            print("Invalid number,Enter a whole number.")

    path_file = 'videogames2.csv'

    with open(path_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file,delimiter='\t')
        writer.writerow(['name', 'gender', 'developer', 'ESRB clasification'])

        for i in range(n):
            print(f"\n Videogame {i+1} ")
            name = input("name: ")
            gender = input("gender: ")
            developer = input("developer: ")
            esrb = input("ESRB clasification: ")
            
            writer.writerow([name, gender, developer, esrb])

    print(f"\n We have seaved {n} videogames in '{path_file}'.")

if __name__ == "__main__":
    input_videogames()
