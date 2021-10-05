from abc import ABC, abstractmethod

#Abstract parent class
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


#child 1
class Car(Vehicle):
    def move(self):
        print("You drive the car")

    def howFast(self,MPH):
        speed = MPH
        print("Woah, you're going {} miles per hour! Slow down!".format(speed))


#child 2
class Boat(Vehicle):
    def move(self):
        print("You drive the boat")

    def howFast(self,MPH):
        speed = MPH
        print("Woah, you're going {} miles per hour! Slow down!".format(speed))


#child 2
class Motorcycle(Vehicle):
    def move(self):
        print("You ride the boat")

    def howFast(self,MPH):
        speed = MPH
        print("Woah, you're going {} miles per hour! Slow down!".format(speed))


Harley = Motorcycle()

Harley.move()
Harley.howFast("500")



