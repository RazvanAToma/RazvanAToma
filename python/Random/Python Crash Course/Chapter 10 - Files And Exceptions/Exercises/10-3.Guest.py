

file_path = "c:/Users/razva/Documents/Python/Python Crash Course/Chapter 10\
 - Files And Exceptions/text_files/"
filename = "guest.txt"


user_name = input("What's your name?\n")

with open(f"{file_path}/{filename}", "w") as file_object:
    file_object.write(f"{user_name}")