""""""
from reader import FileReader
from writer import Writer


def greet_user():
    filename = 'files/username.json'
    try:
        username = FileReader().read(filename)
    except FileNotFoundError:
        # If username doesn't exist
        while True:
            inp_name = input("What's your name?\n-> ")
            if inp_name:
                Writer().write(inp_name, filename)
                print(f"I'll remember you {inp_name}")
                break
            else:
                print("\nError: No text was given. Please enter your name.")
                continue
    else:
        print(f'Hi, {username}!')
