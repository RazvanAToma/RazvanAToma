

def car_info(manufacturer, model_name, **other):
    """Prints dictionary about car."""
    car = {}
    car["manufacturer"] = manufacturer
    car["model_name"] = model_name

    for key, value in other.items():
        car[key] = value
    print(car)

car_info("audi", "RSQ8", color="black", tow_package=True)

