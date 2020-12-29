# Classes are used similarly to how they are in Java. They are object oriented, can be instantiated,
# and possess their own functions and attributes.

# Classes should be named used CamelCase, with capital letters and no underscores.
class Rocket:

    # This is essentially the constructor. Notably, 'self' is a necessary parameter and must be first.
    # Class methods don't implicitly pass their own instance to the method, so this must be done
    # explicitly.
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_up(self):
        self.y += 1


# Basic inheritance: This is the syntax for making Rocket the superclass of Shuttle.
class Shuttle(Rocket):
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed


# Notably, 'new' Rocket() isn't required in Python.
my_rocket = Rocket()
print("Rocket altitude:", my_rocket.y)

my_rocket_2 = Rocket(1, 1)
print("Rocket 2 altitude:", my_rocket_2.y)
my_rocket_2.move_up()
print("Rocket 2 altitude:", my_rocket_2.y)
