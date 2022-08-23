guests = ['Grandfather', 'Grandmother', 'Father']

copy_guests = guests.copy()
for guest in guests:
    index = copy_guests.index(guest)

    if guest == 'Father':
        print("Hello, Father! You want to go dinner with me tomorrow?")
        print(
            "Sorry son, i can't come because tomorrow I'll be at a work trip in Pernambuco.\n")
        copy_guests.remove('Father')
        copy_guests.insert(index, 'Brother')

    message = f"Hello, {copy_guests[index]}! You want to go dinner with me tomorrow?"
    print(message)

guests = copy_guests.copy()
print("I found a new dinner table that is bigger, I'll invite more people!")

guests.insert(0, 'Freddie Mercury')  # Beggining
guests.insert(2, 'Ludwig von Mises')  # Middle
guests.append('Hayek')  # End

copy_guests = guests.copy()
for guest in guests:
    index = copy_guests.index(guest)
    message = f"Hello, {guests[index]}! You want to go dinner with me tomorrow?"
    print(message)

guests = copy_guests.copy()
print("My bigger dinner table won't arrive today, so left only two spaces in my dinner table.")

print(f"\n{guests.pop(5)} you're not invited.")
print(f"{guests.pop(4)} you're not invited.")
print(f"{guests.pop(3)} you're not invited.")
print(f"{guests.pop(2)} you're not invited.\n")

for guest in guests:
    index = guests.index(guest)
    message = f"Hello, {guests[index]}! You're still invited."
    print(message)

print("\n\t End of the program")
