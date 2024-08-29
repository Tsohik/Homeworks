#Create a Python class representing a car with methods for accelerating and braking.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, amount):
        if amount > 0:
            self.speed += amount
            print(f"The car is accelerating. New speed: {self.speed} km/h")

    def brake(self, amount):
        if amount > 0:
            self.speed -= amount
            if self.speed < 0:
                self.speed = 0
            print(f"The car is braking. New speed: {self.speed} km/h")

    def __str__(self):
        return f"{self.year} {self.make} {self.model} going at {self.speed} km/h"

my_car = Car("Toyota", "Camry", 2021)
print(my_car)
my_car.accelerate(50)
print(my_car)
my_car.brake(20)
print(my_car)
my_car.brake(40)
print(my_car)
