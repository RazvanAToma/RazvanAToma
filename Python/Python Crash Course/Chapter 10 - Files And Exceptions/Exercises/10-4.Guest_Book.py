
file_path = "c:/Users/razva/Documents/Python/Python Crash Course/Chapter 10\
 - Files And Exceptions/text_files/"
filename = "guest_book.txt"


while True:
    user_name = input("Name: ")
    with open(f"{file_path}/{filename}", "a") as file_object:
        file_object.write(f"{user_name}\n")

    print(f"Hello, {user_name}, you have been registered in the guest book.")