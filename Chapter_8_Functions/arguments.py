# Default Values:
def lented_book(book="miracle morning", person="Yasmin"):
    """Display the lented book and for who the book was lented"""
    print(f"I lent my book {book.title()} to {person.title()}")


# Positional Arguments:
print("Positional arguments:")

print("\nCorrectly order:")
lented_book("Human Action", "Yasmin")

print("\nIncorrectly order:")
lented_book("Yasmin", "Human Action")

# Keyword arguments:
print("\nKeyword arguments:")

print("\nNo order is needed.")
lented_book(person="Yasmin", book="Human Action")

# Using default values:
print("\nPassing no arguments:")
lented_book()
