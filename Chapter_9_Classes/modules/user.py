class User:
    """
    Represents the user profile from a website.
    """

    def __init__(self, first_name='', last_name=''):
        """
        Assign the atributes first_name and last_name with given
        arguments.
        """
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"Full name: {self.first_name.title()}"
              f" {self.last_name.title()}")

    def greet_user(self):
        print(f"Welcome, {self.last_name.title()}")


user_00 = User("Matheus", "Delmaschio")
user_01 = User("Yasmin", "Delmaschio")
user_02 = User("Sara", "Delmaschio")

user_00.describe_user()
user_00.greet_user()

user_01.describe_user()
user_01.greet_user()

user_02.describe_user()
user_02.greet_user()
