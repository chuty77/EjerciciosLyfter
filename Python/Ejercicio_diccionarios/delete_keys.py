list_of_keys = [
'access_level', 
'age'
]

employee = {
 'name': 'John', 
 'email':'john@ecorp.com', 
 'access_level': 5, 
 'age': 28
 }


for data in list_of_keys:
   employee.pop(data)

   print(employee)