
print("ACTIVITY 1")
# Print a heading for the assignment
print("PLP PYTHON OPP ASSIGNMENT\n")

# Define a base class for all superheroes
class Superhero:
    def __init__(self, name, age, country, strength, power):
        # Initialize superhero attributes
        self.name = name
        self.__real_age = age  # Private attribute using name mangling
        self.country = country
        self.strength = strength
        self.power = power

    def description_of_superhero(self):
        # Display details about the superhero
        print(f"This superhero is called {self.name}.")
        print(f"He is {self.__real_age} years old.")  # Accessing private attribute
        print(f"He comes from {self.country}.")
        print(f"This Superhero can write {self.strength} number of python codes in an hour.")
        print(f"This superhero can transform python codes into {self.power}\n")


# Subclass of Superhero that represents a Python programmer
class Python_Programmer(Superhero):
    def __init__(self, name, age, country, strength, power):
        # Call the parent class constructor
        super().__init__(name, age, country, strength, power)
        print("This is a Python Programmer.")


# Subclass of Superhero that represents a Python teacher
class Python_Teacher(Superhero):
    def __init__(self, name, age, country, strength, power):
        # Call the parent class constructor
        super().__init__(name, age, country, strength, power)
        print("This is a Python Programming Teacher.")


# Create an instance of Python_Programmer
ghana_python_programming_entities = Python_Programmer("Vincent", 32, "Ghana", "billion", "functioning softwares")
# Call method to describe the superhero
print(ghana_python_programming_entities.description_of_superhero())

# Attempt to change private attribute (won't actually affect __real_age due to name mangling)
ghana_python_programming_entities.__real_age = 40

# Reassign the variable to an instance of Python_Teacher
ghana_python_programming_entities = Python_Teacher("Akomeah", 32, "Ghana", "billion", "functioning softwares")
# Call method to describe the superhero
print(ghana_python_programming_entities.description_of_superhero())

print("ACTIVITY 2")
# Define a general class for all moving entities
class Entity:
    def __init__(self, name, form_of_movement):
        self.name = name
        self.form_of_movement = form_of_movement

    def movement_of_entity(self):
        # Print how this entity moves
        print(f"The {self.name} is {self.form_of_movement}")


# Car class inherits from Entity
class Car(Entity):
    def __init__(self, name, form_of_movement):
        super().__init__(name, form_of_movement)


# Bird class inherits from Entity
class Bird(Entity):
    def __init__(self, name, form_of_movement):
        super().__init__(name, form_of_movement)


# Motor class inherits from Entity
class Motor(Entity):
    def __init__(self, name, form_of_movement):
        super().__init__(name, form_of_movement)


# Instantiate and describe a car
tesla = Car("Tesla", "driving.")
print(tesla.movement_of_entity())

# Instantiate and describe a bird
parrot = Bird("Parrot", "flying.")
print(parrot.movement_of_entity())

# Instantiate and describe a motorbike
yamaha = Motor("Motor", "riding.")
print(yamaha.movement_of_entity())
