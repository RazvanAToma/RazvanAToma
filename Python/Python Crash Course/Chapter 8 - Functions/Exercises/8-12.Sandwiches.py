
def make_sandwich(*addons):
    """Print summary of ingredients in sandwich"""
    print("\nMaking a sandwich with:")
    for addon in addons:
        print(f"- {addon}")

make_sandwich("cheese")
make_sandwich("cheese", "ham")
make_sandwich("cheese", "ham", "sauce")

