fav_numbers = {
    'matheus': 8,
    'valdir': 3,
    'davi': 5,
    'jose': 1,
    'joao': 9,
}

for key in fav_numbers:
    print(f"O número favorito de {key.title()} é {fav_numbers.get(key)}")
