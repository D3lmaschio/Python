for n in range(1, 6):
    print(n)

# Making a list of numbers with range() function:
numbers = list(range(1, 11))

for number in numbers:
    print(number)

print("\n")
evens = list(range(2, 11, 2))
print(evens)


# Firt 10 square numbers list:
squares = []
for number in range(1, 11):
    squares.append(number ** 2)

print(f"\n10 first square numbers: {squares}")
