def make_shirt(print_message="T-Shirts are cool.", size="Large"):
    """Display the T-Shirt size and printed text on t-shirt"""
    print(f"Making your T-Shirt:\n"
          f"\tSize: {size}\n"
          f"\tMessage printed: {print_message}")


print("Using posicional arguments:")
make_shirt("Liberty OR Death", "G",)

print("\nUsing keyword arguments:")
make_shirt(size="G", print_message="Liberty OR Death")

print("\nUsing default values:")
make_shirt("I love Python")

print("\nLarge, default message:")
make_shirt(size="Large")

print("\nMedium, default message:")
make_shirt(size="Medium")

print("\nAny size, different message:")
make_shirt(print_message="Python is cool", size="Large")
