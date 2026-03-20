#inside
def inside_number():
    number_for_scope= 8
    return number_for_scope

outside_number = inside_number()
print(outside_number)




#global
y = 5

def global_number():
    global y
    y= 15

global_number()
print(y)


