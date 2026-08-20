class Person:
    def __init__(self,name,age):
        self.name=name #public variables
        self.age=age
    def get_name(person):
        return person.name
person=Person("Nirmal",25)
print(person.name)
# print(dir(person))
        
class Person:
    def __init__(self,name,age):
        self.__name=name #private variables
        self.__age=age
def get_name(person):
    return person.__name
person=Person("Nirmal",25)
# print(get_name(person))


class Person:
    def __init__(self,name,age):
        self._name=name #protected variables
        self._age=age

class Employee(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
    
def get_name(person):
    return person._name
person=Employee("Nirmal Dangi",25)
print(get_name(person))