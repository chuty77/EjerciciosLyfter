
name= input ("Ingrese su nombre ")
last_name= input ("Ingrese su apellido ")
age= int(input ("Ingrese su edad "))


if(age<=5):
    print("Es un niño")
elif (age<12):
    print("Es una pre adolecente") 
elif (age<18):
    print("Es un adolecente") 
elif (age<=30):
    print("Es una adulto joven") 
elif (age<=55):
    print("Es una adulto") 
else:
    print(F"{name} {last_name} Es un adulto mayor porque tiene {age} años")

