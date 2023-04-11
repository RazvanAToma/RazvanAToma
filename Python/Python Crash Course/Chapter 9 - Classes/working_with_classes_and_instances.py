
# The Car Class

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        # Setting a Default Value for an Attribute
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
            """Print a statement showing the car's mileage."""
            print(f"This car has {self.odometer_reading} miles on it.")

    # Modifying an Attribute's Value Through a Method
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

my_new_car = Car("audi", "rsq8", 2020)
print(my_new_car.get_descriptive_name())

# Modifying an Attribute's Value Directly
my_new_car.odometer_reading = "100,000"
my_new_car.read_odometer()

# Modifying an Attribute's Value Through a Method
my_new_car.update_odometer("120,000")
my_new_car.read_odometer()