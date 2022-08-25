heroes = ['Goku', 'Superman', 'Gohan', 'Spider-man']
villains = ['Freeza', 'Goku Black', 'Majin Boo', 'Green Goblin']
anti_heroes = ['Vegeta', 'Bills', 'Deadpool']

characters = heroes[:] + villains[:] + anti_heroes[:]

# for char in characters:
#    print(char)

for char in characters:
    if char in heroes:
        print(f"{char.title()} is a hero!\n")

    elif char in anti_heroes:
        print(f"{char.title()} is a anti-hero!\n")

    else:
        print(f"{char.title()} is a villain!\n")
