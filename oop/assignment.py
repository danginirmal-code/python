class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
class Dog(Animal):
    def __init__(self,name,species,breed):
        super().__init__(name,species)
        self.breed=breed

# dog = Dog('Buddy', 'Canine', 'Golden Retriever')
# print(dog.name, dog.species, dog.breed)

class Dog(Animal):
    def __init__(self,name,species,breed):
        super().__init__(name,species)
        self.breed=breed
    def __str__(self):
        return f"Dog(Name: {self.name}, Species: {self.species}, Breed: {self.breed})"

# dog = Dog('Buddy', 'Canine', 'Golden Retriever')
# print(dog)


class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")
# dog = Dog('Buddy', 'Canine', 'Golden Retriever')
# dog.bark()

class Walker:
    def walk(self):
        print("Walking...")

class Runner:
    def run(self):
        print("Running...")

class Athlete(Walker, Runner):
    pass
# athlete = Athlete()
# athlete.walk()
# athlete.run()


class Athlete(Walker, Runner):
    def walk(self):
        print("Athlete walking...")
        super().walk()

# Test
# athlete = Athlete()
# athlete.walk()

class Athlete(Walker, Runner):
    def __init__(self, training_hours):
        self.training_hours = training_hours

    def train(self):
        print(f"Training for {self.training_hours} hours.")