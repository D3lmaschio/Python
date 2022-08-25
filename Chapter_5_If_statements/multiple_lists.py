available_toppings = [
    'mushrooms', 'olives', 'green peppers',
    'pepperoni', 'pineapple', 'extra cheese'
]

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

pizza_toppings = []

for req_top in requested_toppings:
    if req_top in available_toppings:
        print(f"Adding {req_top}...")
    else:
        print(f"We don't have {req_top}.")

print("\nYour pizza is finished!")
