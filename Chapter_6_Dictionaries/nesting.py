# List of dictionaries

print("\n-------------------------------")
print("List of Dictionaries:\n")

aliens = []

# Making a new alien for each loop:
for qtd_aliens in range(30):
    alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(alien)

# Slicing a list in 3 elements ( [:3] ) and modifying each element:
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")

# Lists inside a Dictionarie

print("\n-------------------------------")
print("Lists inside a Dictionarie:\n")

pizza_ordered = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza_ordered.get('crust')}-crust pizza "
      "with the following toppings:")

for topping in pizza_ordered.get('toppings'):
    print("\t" + topping.title())

print("\nAnother example:")

programmers = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for programmer, langs in programmers.items():
    if len(langs) > 1:
        print(f"\n{programmer.title()}'s favorite languages are:")

        for lang in langs:
            print(f"\t{lang.title()}")

    else:
        print(
            f"\n{programmer.title()}'s favorite language is {langs[0].title()}.")

print("\n-------------------------------")
print("Dictionaries inside a Dictionarie:")

#  Dictionaries inside Dictionarie:

users = {
    'user_00': {
        'first': 'matheus',
        'last': 'delmaschio',
        'location': 'brazil',
    },

    'user_01': {
        'first': 'yasmin',
        'last': 'delmaschio',
        'location': 'brazil',
    }
}

for user, info in users.items():
    print(f"\nUsername: {user.title()}")
    full_name = f"{info['first']} {info['last']}"
    location = info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
