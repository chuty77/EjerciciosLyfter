name=  'paulo'
surname= 'quiros'

print(name+surname)

name=  'paulo'
age= 27
#print(nombre+edad)
#TypeError: can only concatenate str (not "int") to str
print(name+str(age))


name=  'quiros'
age= 27
#print(edad+nombre)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(f"Mi edad es {age} y mi apellido es {name}")



list_of_integers = [4, 7, 3, 5 + 4, 3]
list_of_strings = ["Hello", "I'm", "A", "String", "List"]

#print(list_of_integers[3]+list_of_strings)
#TypeError: unsupported operand type(s) for +: 'int' and 'list'
print(f"{list_of_integers[3]} {list_of_strings[3]}")


name=  'paulo'
list_of_integers = [4, 7, 3, 5 + 4, 3]
#print(name+list_of_integers)
#TypeError: can only concatenate str (not "list") to str
print(f"{name } {list_of_integers[0]}")


salary=  20.80
age= 27
print(salary+age)

