from modules.reader import FileReader
from modules.writer import Writer

w = Writer()

while True:
    inp_name = input("What's your name?\n> ")
    w.write("\n" + inp_name, 'files/guests.txt')
    print(f"\nWelcome, {inp_name}!\n")

    content = FileReader().read('files/guests.txt').get_content()
    print(f"-> Guest book:{content}")

    repeat = input("\nDo you want to enter a new name? (y/n)\n> ")
    if repeat != 'y':
        break
