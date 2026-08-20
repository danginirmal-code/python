class Animal:
    def speak(self):
        return "Sound of the animal"
class Dog(Animal):
    def speak(self):
        return "woof"
class Cat(Animal):
    def speak(self):
        return "meow"
dog=Dog()
cat=Cat()
print(dog.speak())
print(cat.speak())

##Polymorphism with functions and methods
class Shape:
    def area(self):
        return f"the area of the figure "
    #derived class
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius


def  print_area(shape):
    print(f"the area is {shape.area()}")
rectangle=Rectangle(4,5)
circle=Circle(3)
print_area(rectangle)
print_area(circle)

##Abstract class
from abc import ABC ,abstractmethod

##Define an abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
#Derived class 1
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"

#create object of car and motorcycle
car=Car()
motorcycle=Motorcycle()
def start_vehicle(vehicle):
    print(vehicle.start_engine())

start_vehicle(car)

