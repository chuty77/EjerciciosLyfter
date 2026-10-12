# Cree una clase Rectangle que:
# Tenga atributos width y height
# Tenga un método get_area() que retorne el área
# Tenga un método get_perimeter() que retorne el perímetro
# Valide que ningún valor sea negativo. Si lo es, 
# lance una excepción con un mensaje adecuado

class Rectangle():

    def __init__(self,width,height):

        if(width < 0):
            raise ValueError("El width no puede ser un número negativo.")
        elif(height < 0):
            raise ValueError("El height no puede ser un número negativo.")
        self.width = width
        self.height = height
        


    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.width) + (self.height + self.height)


def add_measures(rectangles):
    
    while True:
        width= int(input("Por favor agregar el width: "))
        height= int(input("Por favor agregar el height: "))
        try:
            rectangle_1= Rectangle(width,height)
            rectangles.append(rectangle_1)   
            break
        except ValueError as error:
            print(f"Existe un valor negativo, los valores deben ser positivos")    
    
rectangles = [] 
add_measures(rectangles)
rectangle_2 = rectangles[0]
print(rectangle_2.get_area())
print(rectangle_2.get_perimeter())


# Cree una clase base Animal y dos clases hijas Dog y Cat:
# Animal debe tener nombre y método speak() que retorne "Hace un sonido"
# Dog debe sobrescribir speak() para decir "Guau"
# Cat debe sobrescribir speak() para decir "Miau"
# Ejemplo
# dog = Dog("Firulais")
# print(dog.speak())  # Guau


class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Hace un sonido"

    
class Dog(Animal):
    def speak(self):
        return "Guau"


class Cat(Animal):
    def speak(self):
        return "Miau"
    

dog = Dog("Firulais")
cat= Cat("Misifus")
print(cat.name)
print(f"{cat.name} dice {cat.speak()}")
print(dog.speak())


# Cree una clase Product con:
# Nombre, precio y cantidad
# Cree una clase Inventory que:
# Guarde productos en una lista
# Tenga métodos para:
# Agregar un producto
# Mostrar todos los productos
# Calcular el valor total del inventario


class Product:
    def __init__(self, name, price, quantity):
        self.name= name
        self.price= price
        self.quantity= quantity



class Inventory():

    def __init__(self):
        self.products = []


    def add_product(self, product):
        self.products.append(product)


    def shows_products(self):
        for i, prod in enumerate(self.products, start=1):
            print(f"[{i}] Name {prod.name}, price {prod.price}, quantity {prod.quantity}")
        


    def calculate_total_value_of_inventory(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total


product_1 = Product("Mouse", 50, 5)
product_2 = Product("Teclado", 100, 2)

inventory_1 =Inventory()
inventory_1.add_product(product_1)
inventory_1.add_product(product_2)
inventory_1.shows_products()
print(inventory_1.calculate_total_value_of_inventory())
