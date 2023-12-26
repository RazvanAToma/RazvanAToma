
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes restaurant"""
        print(f"The restaurants name is {self.restaurant_name}.")
        print(f"It serves {self.cuisine_type.title()} cuisine.")
    
    def open_restaurant(self):
        """Says if restaurant is open."""
        print(f"{self.restaurant_name} is open!")


restaurant = Restaurant("Gustau's", "french")
restaurant.open_restaurant()
restaurant.describe_restaurant()