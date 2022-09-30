""""""
from os.path import exists as path_exists
from .reader import FileReader
from .writer import Writer


USR_PATH = 'files/username.txt'


def create_user():
    """Ask for username"""
    while True:
        # Ask for user to enter his username
        username = input("Enter your username: ")

        # Verifying if some text is entered
        if username:
            # Writing the text to the file USR_PATH in .json
            Writer().write((username + '\n'), USR_PATH)
            print(f"I'll remember you {username}")
            break
        else:
            print("\nError: No text was given. Please enter your username.")
            continue


def user_exists(username):
    """Verify if given username exists in username.json"""
    if path_exists(USR_PATH):
        usernames = FileReader().read(USR_PATH).get_content()\
                                               .replace('\n', '')
        if usernames:
            return username if username in usernames else None
    return None


def greet_user():
    """Greets the user."""
    inp_username = input("Enter your username: ")

    username = user_exists(inp_username)
    if username:
        print(f"\nWelcome back, Mr(s).{username.rstrip().title()}!")
    else:
        # If username doesn't exist
        print(f"\nusername: {inp_username} doens't exists."
              " Initiating username registering process...")
        create_user()
