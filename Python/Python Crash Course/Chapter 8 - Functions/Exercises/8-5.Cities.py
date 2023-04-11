
def describe_city(name="reykjavik", country="iceland"):
    """Display information about city"""
    print(f"{name.title()} is in {country.title()}")

# Calling function with default values
describe_city()

# Calling function with positional arguments
describe_city("oslo", "norway")

# Calling function with keyword arguments
describe_city(name="stockholm", country="sweden")
