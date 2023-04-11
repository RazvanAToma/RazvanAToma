
# List with sandwiches that are ordered
#  Empty list with finished sandwiches
sandwich_orders = ["pastrami", "tuna", "pastrami", "ham", "pastrami", "cheese"]
print(sandwich_orders)
finished_sandwiches = []

# No pastrami
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)

# Moving made sandwiches over to finished sandwiches list.
while sandwich_orders:
    in_making = sandwich_orders.pop()
    print(f"\nThe {in_making.title()} sandwhich is being made!")

    finished_sandwiches.append(in_making)
    print(f"The {in_making.title()} sandwhich is finished")

# Show sandwhiches made so far.
print("\n")
for sandwich in finished_sandwiches:
    print(f"We made a {sandwich} sandwich")