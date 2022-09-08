from random import randint
from random import choice

# radint method generates a pseudorandom number with the given range():
random_number = randint(1, 100)
print(f"Using randint method from random module:"
      f"\nRandom int between 1 and 100: {random_number}")

# choice method "choice" a random element from the given non-empty sequence:
lista_teste = list(range(1, 10))
random_element = choice(lista_teste)
print(f"\nUsing choice method from random module:"
      f"\nRandom element from lista_teste: {random_element}")
