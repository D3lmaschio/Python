languages = [
    'python', 'java', 'php',
    'r', 'c', 'c++'
]

print("Raw:")
print(languages)

# Lembre-se que o index começa do 0!
slices = languages[0:3]
print("\nSlice [0:3]:")
print(slices)

slices_2 = languages[1:5]
print("\nSlice [1:5]:")
print(slices_2)

# omitindo o index 0.
slices_3 = languages[:2]
print("\nSlice [:2]")
print(slices_3)

# omitindo o último index da lista
slices_4 = languages[3:]
print("\nSlice [3:]:")
print(slices_4)

# Relembrando sobre o index negativo:
slices_5 = languages[-3:]
print("\nSlice [-3:]:")
print(slices_5)

slices_6 = languages[::2]
print("\nSlice [::2]")
print(slices_6)

# Looping through a slice
print("\nLooping through a slice [:3]:")
for lang in languages[:3]:
    print(f"Eu vou aprender {lang.title()}!")

print("\nLooping through a slice [-3:]:")
for lang in languages[-3:]:
    print(f"Eu ainda não vou aprender {lang.title()}!")
