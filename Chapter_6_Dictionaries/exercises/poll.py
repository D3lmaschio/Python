favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'joao': 'r',
}

for person in favorite_languages:
    fav = favorite_languages.get(person)
    print(f"A linguagem de programação \
        \nfavorita de {person.title()} é: {fav.title()}!\n")

to_poll = ['pedro', 'maria', 'jorge', 'jen', 'sarah', 'edward']

for person in to_poll:
    if person not in favorite_languages.keys():
        print(f"You should take the poll {person.title()}!")
    else:
        print(f"Thank you for responding {person.title()}!")
