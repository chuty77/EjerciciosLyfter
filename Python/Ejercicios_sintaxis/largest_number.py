num1= int(input ("Ingrese un numero"))
num2= int(input("Ingrese segundo numero"))
num3=int (input("Ingrese terver numero"))

if(num1 > num2 and num1 > num3):
  print (f"El primer numero es el mayor {num1}")
elif(num2>num1 and num2>num3):
  print (f"El segundo numero es el mayor {num2}")
elif(num3>num1 and num3>num2):
  print (f"El tercer numero es el mayor {num3}")
else:
  print (f"Ningun numero es mayor que otro")  