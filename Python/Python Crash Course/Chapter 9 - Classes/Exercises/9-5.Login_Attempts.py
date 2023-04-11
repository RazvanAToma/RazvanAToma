
class User():

    def __init__(self, first_name, last_name, **other):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.other = other
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


razvan = User("razvan", "toma", height=174)
razvan.describe_user()
razvan.greet_user()

while razvan.login_attempts != 10:
    razvan.increment_login_attempts()
print(razvan.login_attempts)

razvan.reset_login_attempts()
print(razvan.login_attempts)