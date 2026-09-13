# object oriented programming

class Person: # blueprint for creating person objects
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def greet(self): #function to greet
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def birthday(self): #function to celebrate birthday
        self.age += 1
        return f"Happy Birthday {self.name}! You are now {self.age} years old."

p1 = Person("Alice", 55) # create an instance
p2 = Person("Bob", 35) # create another instance


# print(p1.birthday()) # call the birthday method of the Person class
# print(p2.birthday()) # call the birthday method of the Person class


# second example of oop

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f" {self.make} {self.model} {self.year}"

    def start_engine(self):
        return f"The engine of the {self.description()} is now running."
    
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

print(car1.description()) # call the description method of the Car class
print(car2.start_engine()) # call the start_engine method of the Car class