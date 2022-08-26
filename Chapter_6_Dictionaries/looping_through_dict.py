person = {
    'name': 'matheus',
    'age': '19',
    'profession': 'ti support',
}

# Looping through a dict by it's KEYS AND VALUES:
print("For each KEY and VALUE:")
for key, value in person.items():
    print(f"KEY: {key}, VALUE: {value}\n")

# Looping through a dict by it's KEYS:
print("For each KEY:")
for key in person:
    print(f"KEY: {key}\n")

# Looping through a dict by it's VALUES:
print("For each VALUE:")
for value in person.values():
    print(f"VALUE: {value}\n")
