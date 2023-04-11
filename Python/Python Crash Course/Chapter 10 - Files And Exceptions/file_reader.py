
# Reading an Entire File

file_path = "c:/Users/razva/Documents/Python/Python Crash Course/Chapter 10\
 - Files And Exceptions/text_files/pi_digits.txt"

with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())


# Reading Line by Line

file_path2 = "c:/Users/razva/Documents/Python/Python Crash Course/Chapter 10\
 - Files And Exceptions/text_files"
filename = "pi_digits.txt"

with open(f"{file_path2}/{filename}") as file_object:
    for line in file_object:
        print(line.rstrip())



# Making a List of Lines from a File
# Working with a File's Contents

with open(f"{file_path2}/{filename}") as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))