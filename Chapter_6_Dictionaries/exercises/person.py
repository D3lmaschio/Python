person = {
    'first_name': 'matheus',
    'last_name': 'delmaschio',
    'age': '19',
    'city': 'guarulhos',
}

for key in person:
    data = person.get(key)

    if key == 'first_name':
        print(f"Nome:{data.title()}")
    elif key == 'last_name':
        print(f"Sobrenome:{data.title()}")
    elif key == 'age':
        print(f"Idade:{int(data)}")
    elif key == 'city':
        print(f"Cidade:{data.title()}")
