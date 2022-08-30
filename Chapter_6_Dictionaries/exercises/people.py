person_00 = {
    'first name': 'matheus',
    'last name': 'delmaschio',
    'age': 19,
    'city': 'guarulhos',
}

person_01 = {
    'first name': 'yasmin',
    'last name': 'delmaschio',
    'age': 20,
    'city': 'guarulhos',
}

person_02 = {
    'first name': 'Jeremy',
    'last name': 'delmaschio',
    'age': 0,
    'city': 'Potirendaba',
}

people = [person_00, person_01, person_02]

for person in people:
    for info, value in person.items():

        if info == 'first name':
            first_name = value
        elif info == 'last name':
            last_name = value
        elif info == 'age':
            age = value
        elif info == 'city':
            city = value
    full_name = f"{first_name} {last_name}"
    print(f"Full name: {full_name.title()}\n"
          f"\tAge: {age}\n"
          f"\tCity: {city.title()}\n")
