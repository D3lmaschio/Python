cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Raw list:")
print(cars)

# Permanent change in the list cars
cars.sort()
print("\nSorting the list cars with sort() method:")
print(cars)

print("\nSorting the list in reverse alphabetical with parameter reverse=True")
cars.sort(reverse=True)
print(cars)

print("\nUsing built-in sorted() method to order a list not permanently: ")
print(sorted(cars))
