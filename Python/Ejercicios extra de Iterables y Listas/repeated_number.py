my_list= []


number_to_look= int(input(f"Ingrese numero a buscar: "))
for i in range(5):
 while True:
  try:
    enter_numbers= int(input(f"Ingresar un numero para la lista: "))
    my_list.append(enter_numbers)
    break
  except ValueError:
   print("Ingrese un numero correcto")

print(f"El número {number_to_look} aparece {my_list.count(number_to_look)} veces")
  
 

