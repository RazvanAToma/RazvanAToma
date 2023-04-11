
# Writing to an Empty File

file_path = "c:/Users/razva/Documents/Python/Python Crash Course/Chapter 10\
 - Files And Exceptions/text_files/"
filename = "programming.txt"

with open(f"{file_path}/{filename}", "w") as file_object:
    file_object.write("I love programming.")



# Writing Multiple Lines

file_path = "c:/Users/razva/Documents/Python/Python Crash Course/Chapter 10\
 - Files And Exceptions/text_files/"
filename = "programming.txt"

with open(f"{file_path}/{filename}", "w") as file_object:
    file_object.write("I love programming.")
    file_object.write("\nI love creating new games.")



# Appending to a File

with open(f"{file_path}/{filename}", "a") as file_object:
    file_object.write("\nI also love finding meaning in large datasets.")
    file_object.write("\nI love creating apps that can run in a browser.")

