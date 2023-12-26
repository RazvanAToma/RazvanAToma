
class User():

    def __init__(self, first_name, last_name, **other):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.other = other

    def describe_user(self):
        """Prints a summary about the user."""
        user = {}
        user["first_name"] = self.first_name
        user["last_name"] = self.last_name
        for key, value in self.other.items():
            user[key] = value

        print(user)
        for key, value in user.items():
            print(f"{key.title()}: {value}")

    
    def greet_user(self):
        """Prints a simple greeting to the user."""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")

razvan = User("razvan", "toma", height=174)
razvan.describe_user()
razvan.greet_user()