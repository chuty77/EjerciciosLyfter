

import random

while True:
   random_number = random.randint(1,10)
   number = int(input("Ingrese un numero del 1-10 para adivinar el numero secreto"))
   try:
     if (number==random_number):
           break 
     else:
           print("Numero incorrecto, vuelva a intentar")
   except ValueError:
     print("Dato invalido, por favor ingrese un entero.")

print(f"Adivinaste el numero secreto es: {number}")
