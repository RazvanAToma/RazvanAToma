
# Polling flag
polling_active = True

# Defining directory
dream_vacation = {}

# Poll
while polling_active:
    # Acquires name
    name = input("What is your name?\n")

    # Acquires dream vacation
    response = input("\nIf you could visit one place in the world, where would \
you go?\n")
    
    # Adding info to directory
    dream_vacation[name] = response

    # Repeat?
    repeat = input("\nWould you like to let someone else anwser the poll? (Y/N)\n").upper()
    if repeat == "N":
        polling_active = False

# Poll Results
print("\n--- Poll Results ---")
for name, response in dream_vacation.items():
    print(f"\n{name.title()} would like to go to {response.title()}")
