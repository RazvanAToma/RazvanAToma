
# Creating the Dog Class

class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")
    
    def roll_over(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} rolled over!")



# Making an Instance from a Class

my_dog = Dog("willie", 6)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")



# Calling Methods

my_dog.sit()
my_dog.roll_over()



# Creating Multiple Instances
print("")
my_dog = Dog("jackson", 6)
your_dog = Dog("wilma", 3)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name.title()}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()