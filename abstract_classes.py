from abc import ABC, abstractmethod

#Abstract parent class
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

#child class
class Car(Vehicle):
    def move(self):
        print("You drive the car")

#child class
class Boat(Vehicle):
    def move(self):
        print("You drive the boat")

#child
class Motorcycle(Vehicle):
    def move(self):
        print("You ride the boat")


Harley = Motorcycle()

Harley.move()



