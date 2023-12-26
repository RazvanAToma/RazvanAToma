
# How the input() Function Works

message = input("Tell me something, and I will repeat it back you: ")
print(message)



# Writing Clear Prompts

name = input("Please enter your name: ")
print(f"Hello, {name}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")



# Using int() to Accept Numerical Input

height = input("How tall are you, in centimeters? ")
height = int(height)

if height >= 50:
    print("\n You're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older")


heightbutbetter = int(input("How tall are you, in centimeters? "))

if heightbutbetter >= 50:
    print("\n You're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older")



# The Modulo Operator

number = int(input("Enter a number, and I'l tell you if it's even or odd: "))

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
elif number % 2 != 0:
    print(f"\nThe number {number} is odd.")