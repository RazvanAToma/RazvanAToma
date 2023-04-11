number = int(input("Input a number and I will tell you if it's a multiple of ten! "))

if number % 10 == 0:
    print(f"The number {number} is a multiple of ten!")
elif number % 10 != 0:
    print(f"The number {number} is not a multiple of ten!")
    