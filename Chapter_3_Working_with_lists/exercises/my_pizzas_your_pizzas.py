my_pizzas = ['peperoni', 'bauru', 'napolitana']
friend_pizzas = my_pizzas[:]

my_pizzas.append('cheese')
friend_pizzas.append('chicken')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

