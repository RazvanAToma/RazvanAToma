

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello {name.title()}!"
        print(msg)

usernames = ["hannah", "ty", "margot"]
greet_users(usernames)



# Modifying a List in a Function

## Start with some designs that need to be printed.
unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

## Simulate printing each design, until none are left.
##  Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()

    ## Simulate creating a 3D print from the design.
    print(f"Printing model: {current_design}.")
    completed_models.append(current_design)

## Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)



# Preventing a Function from Modifying a List

