pet_00 = {'name': 'roberto', 'owner': 'pedro', 'kind': 'lizard', }
pet_01 = {'name': 'joffrey', 'owner': 'peter', 'kind': 'bird', }
pet_02 = {'name': 'billy', 'owner': 'john', 'kind': 'cat', }
pet_03 = {'name': 'scooby', 'owner': 'salsicha', 'kind': 'dog'}

pets = [pet_00, pet_01, pet_02, pet_03, ]

for pet in pets:
    for info, value in pet.items():
        if info == 'name':
            name = value
        elif info == 'owner':
            owner = value
        elif info == 'kind':
            kind = value
    print(f"Kind: {kind.title()} | Name: {name.title()} |"
          f" Owner: {owner.title()}")
