
list_numbers= []


for i in range(10):
 while True:
    try:
         number = int(input(f"Ingrese el numero {i+1} de 10: "))
         list_numbers.append(number)
         break            
    except ValueError:
     print("Dato invalido, por favor ingrese un entero.")

highest_number= max(list_numbers)
print(f"El número mayor es: {highest_number}")
