def make_sandwich(*ingredients, sandwich=None):
    if ingredients:
        sandwich = []
        for ingredient in ingredients:
            sandwich.append(ingredient)
            print(f"Adding {ingredient.title()}...")

        print("Your sandwich is ready!")
        return sandwich
    else:
        return sandwich


sanduba = make_sandwich('hamburguer',
                        'cheddar', 'sauce', 'bread')

print("\nYour sandwich:")
for ingr in sanduba:
    print(f"\t{ingr.title()}")
