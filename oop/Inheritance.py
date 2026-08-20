class Car:
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
    def drive(self):
        print(f"The person will drive the {self.enginetype}")

car1=Car(3,4,"petrol")
car1.drive()

class Tesla(Car):
    def __init__(self,windows,doors,enginetype,isSelfDriving):
        super().__init__(windows,doors,enginetype)
        self.isSelfDriving=isSelfDriving
    def selfdriving(self):
        print("tesla supports self driving",self.isSelfDriving)
tesla1=Tesla(4,5,"electric",True)
tesla1.selfdriving()
tesla1.drive()

#Multiple Inheritance
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Subclass must implement this method")
class Pet:
    def __init__(self,owner):
        self.owner=owner
#derive class
class Dog(Animal,Pet):
    def __init__(self,name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)
    def speak(self):
        return f'{self.name} say woof'

dog=Dog("Nudy","Krish")
print(dog.speak())