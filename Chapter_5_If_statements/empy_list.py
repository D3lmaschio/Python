requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        if topping in requested_toppings:
            print(f"Adding {topping}...")
        else:
            print(f"Sorry we don't have {topping}.")
else:
    print("Are you sure you want plane pizza?")
