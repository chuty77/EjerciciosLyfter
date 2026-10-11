import math
# Cree una clase de Circle con:
# Un atributo de radius (radio).
# Un método de get_area que retorne su área.
class Circle ():

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area=  math.pi * (self.radius **2)
        return area

        
circle_1 = Circle(100)
print (f"The area is: {circle_1.get_area()}")

# Cree una clase de Bus con:
# Un atributo de max_passengers.
# Un método para agregar pasajeros uno por uno 
# (que acepte como parámetro una instancia de la clase Person vista en la lección).
#  Este solo debe agregar pasajeros si lleva menos de su máximo. 
# Sino, debe mostrar un mensaje de que el bus está lleno.
# Un método para bajar pasajeros uno por uno (en cualquier orden).


class Person():
    def __init__(self, name):
        self.name = name     


class Bus():

    def __init__(self,capacity):
        self.capacity= capacity
        self.max_passengers= []


    def bus_full(self):
        return len(self.max_passengers) >= self.capacity


    def add_passenger(self,person):
        if self.bus_full() == False:
            self.max_passengers.append(person.name)
        else:
            print("The bus is full")

    def remove_passenger(self, person):
        if  len(self.max_passengers) >=  self.capacity:
            self.max_passengers.remove(person.name)
        

bus_1=  Bus(3)
bus_1.add_passenger(Person("Juan"))
bus_1.add_passenger(Person("Paulo"))
bus_1.add_passenger(Person("Maria"))
print(bus_1.max_passengers)
bus_1.remove_passenger(Person("Paulo"))
print(bus_1.max_passengers)


# Cree las siguientes clases:
# Head
# Torso
# Arm
# Hand
# Leg
# Feet
# Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.
# Por ejemplo (este código esta incompleto, pero describe la idea):

class Human:
    def __init__(self, torso):
        self.torso= torso        

class Head:
    def __init__(self):
        pass

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.right_leg = right_leg
        self.left_arm= left_arm
        self.left_leg =left_leg

class Arm:
    def __init__(self, hand):
        self.hand = hand


class Hand:
    def __init__(self):
        pass


class Leg:
    def __init__(self, feet):
        self.feet = feet


class Feet:
    def __init__(self):
        pass



head = Head()
## Arms and hands
right_hand = Hand()
left_hand = Hand()
right_arm = Arm(right_hand)
left_arm= Arm(left_hand)
## Legs anb feets
left_feet= Feet()
right_feet= Feet()
left_leg= Leg(left_feet)
right_leg= Leg(right_feet)
##Torso
torso = Torso(head, right_arm, left_arm, right_leg,left_leg )
human= Human(torso)
print(human.torso)
print(right_hand)
print(human.torso.right_arm.hand)