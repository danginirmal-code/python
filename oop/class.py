class Car:
    pass
audi=Car()
print(type(audi))
audi.windows=5
print(audi.windows)

class Dog:
    ##constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
##Create a objects
dog1=Dog("Nirmal",25)
print(dog1.name,dog1.age)



class Dog:
    ##constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(f'{self.name} says woof')
##Create a objects
dog1=Dog("Nirmal",25)
dog1.bark()
print(dog1.name,dog1.age)

##Modeling a Bank account

#define a class for bank account
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is deposited .New balance is {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print('Insufficient funds')
        else:
            self.balance-=amount
            print(f"{amount} is withdrawn New balance is {self.balance}")
    def get_balance(self):
        return self.balance
account=BankAccount("Krish",5000)
print(account.balance)

        
