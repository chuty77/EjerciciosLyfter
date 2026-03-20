
def division(a, b):
    if b == 0:
        print("Error: You cannot divide by zero.")
        return a
    return a / b


def addition(a, b): 
    return a + b


def multiplication(a, b): 
    return a * b


def subtract(a, b): 
    return a - b



def calculadora():
    current = 0.0
    
    while True: 
        print(f"Current number: {current}")
        print("1. Addition\n2. Subtract\n3. Multiplication\n4. Division\n5. Erase result\n6. Exit")
        
        option = input("Choose an option from (1-6): ")
        
        if option == '5':
            current = 0.0
            continue
        elif option == '6':
            break
        elif option not in ['1', '2', '3', '4']:
            print("Invalid option.")
            continue

        try:
            new_num = float(input("Enter a new number: "))
        except ValueError:
            print("Error: You entered a invalid number.")
            continue

        if option == '1': current = addition(current, new_num)
        elif option == '2': current = subtract(current, new_num)
        elif option == '3': current = multiplication(current, new_num)
        elif option == '4': current = division(current, new_num)

if __name__ == "__main__":
    calculadora()
