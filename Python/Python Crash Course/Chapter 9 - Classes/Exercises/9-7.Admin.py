
class User():

    def __init__(self, first_name, last_name, **other):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.other = other
        self.login = Login()
        self.admin = Admin()

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
    

class Login():
    """A simple attempt to make a model to count login attempts."""

    def __init__(self, login_attempts=0):
        "Initialize attributes"
        self.login_attempts = login_attempts

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    """Represents a special type of user."""

    def __init__(self, privileges=[]):
        """Initialize attributes"""
        self.privileges = privileges

    def give_privileges(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("The admin has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

razvan = User("razvan", "toma", height=174)
razvan.describe_user()
razvan.greet_user()

while razvan.login.login_attempts != 10:
    razvan.login.increment_login_attempts()
print(razvan.login.login_attempts)

razvan.login.reset_login_attempts()
print(razvan.login.login_attempts)

razvan.admin.give_privileges()
print(razvan.admin.show_privileges())