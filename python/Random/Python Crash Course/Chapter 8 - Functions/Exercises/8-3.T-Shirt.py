
def make_shirt(size, text):
    """Display information about the T-Shirt"""
    print(f"The T-Shirt is size {size.title()} and it has the text {text}")

# Calling function using positional arguments
make_shirt("M", "Trump 2024")

# Calling function using keyword arguments
make_shirt(size="m", text="Trump 2024")