sandwich_orders = [
    'sanduíche de presunto', 'sanduíche de frango',
    'sanduíche de peito de peru', 'pastrami',
    'sanduíche monstruoso', 'pastrami', 'tuna sandwich',
    'pastrami',
]

finished_sandwiches = []

print("Deli run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I made your {sandwich.title()}")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)
