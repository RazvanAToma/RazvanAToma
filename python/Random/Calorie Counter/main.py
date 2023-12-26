

database = {'cheese': {"caloriesPr100g": 250,"proteinPr100g": 10},
            'butter': {"caloriesPr100g": 500,"proteinPr100g": 5},
            'chicken': {"caloriesPr100g": 350,"proteinPr100g": 25},
            'bread': {"caloriesPr100g": 250,"proteinPr100g": 15}
}

ingredients = {}
totalCalories = 0

while True:
    ingredient = str(input("What did you eat? ").lower())
    
    if ingredient == 'stop':
        break
    else:
        ingredients[ingredient] = 0
        print('\n')
        

print(ingredients)

for ingredient in ingredients:
    grams = int(input(f"How much {ingredient} did you use / eat:"))
    ingredients[ingredient] = grams

print(ingredients)


for ingredient in ingredients:
    grams = ingredients[ingredient]
    if ingredient in database:
        caloriesEaten = database[ingredient]["caloriesPr100g"]*grams/100
        print(f"You ate {caloriesEaten} calories of {ingredient}")
        totalCalories = totalCalories + caloriesEaten
    else:
        print(f"{ingredient} is not in the database")

print(f"You ate a total of {totalCalories} calories")