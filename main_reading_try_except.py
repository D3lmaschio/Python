from modules.reader import FileReader

r = FileReader()

try:
    cats_txt = r.read('files/cats.txt').get_content()
    dogs_txt = r.read('files/dogs.txt').get_content()
except FileNotFoundError:
    # print("\nError: one of these files doesn't exist.")
    pass
else:
    print(f"Cats:\n{cats_txt}")
    print(f"Dogs:\n{dogs_txt}")
