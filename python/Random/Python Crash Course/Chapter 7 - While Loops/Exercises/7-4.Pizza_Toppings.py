
prompt = "Enter a pizza topping: "
prompt += "\n(Type 'quit' to exit)"

while True:
    topping = input(prompt)
    if topping == "quit":
        break
    else:
        print(f"We'll add {topping} to your pizza!")