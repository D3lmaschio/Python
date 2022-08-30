pets = {
    'dogs': {
        'scooby': {
            'owner': 'salsicha',
            'age': 2,
        },
        'fred': {
            'owner': 'anthony',
            'age': 4,
        },
    },

    'birds': {
        'joffrey': {
            'owner': 'peter',
            'age': 1,
        },
        'jimmy': {
            'owner': 'freud',
            'age': 2
        },
    },

    'cats': {
        'billy': {
            'owner': 'john',
            'age': 7,
        },
        'pedro': {
            'owner': 'julio',
            'age': 9,
        },
    },
}

for kind, pet in pets.items():
    print(f"Kind: {kind.title()}")

    for pet_name, about in pet.items():
        print(f"\tPet: {pet_name.title()}")

        for info, value in about.items():
            if info == 'owner':
                owner = value
            elif info == 'age':
                age = value
        print(f"\t\tOwner: {owner.title()}")
        print(f"\t\tAge:{age}\n")
