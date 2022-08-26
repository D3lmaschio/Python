poll = {
    'jorge': 'lula',
    'antonio': 'bolsonaro',
    'julio': 'bolsonaro',
    'jonas': 'lula',
}
# usando set() para que os values não se repitam.
for value in set(poll.values()):
    print(f"Value: {value}\n")
