
mile = 1.60934

gallon = 3.78541

mpg = float(input("Input how many miles your car goes per gallon: "))

km = mpg * mile

print(f"Per 100 kilometers, your car consumes {100/(km/gallon)} liters")