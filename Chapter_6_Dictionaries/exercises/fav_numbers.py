fav_numbers = {
    'matheus': [8, 9],
    'valdir': [3, 2],
    'davi': [5, 4],
    'jose': [1, 7],
    'joao': [9, 8],
}

for name, number in fav_numbers.items():
    if len(number) <= 1:
        print(f"{name.title()}'s favorite number is: {number}")
    else:
        print(f"{name.title()}'s favorite numbers are:")
        for num in number:
            print(f"\t{num}")
