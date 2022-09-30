from os.path import exists as path_exists
from modules.file import store, load


FILENAME = 'files/favorite_number.json'

if path_exists(FILENAME):
    number = load(FILENAME)
    print(f"I remember that your favorite number is: {number}")
else:
    inp_number = input("What's your favorite number?\n> ")
    store(inp_number, 'files/favorite_number')
