class Restaurant:

    def __init__(self, res_name, cuisine_type=None):
        """
        Intialize the class with restaurant name and cuisine type
        as arguments.
        """
        self.name = res_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.cuisine_type} restaurant {self.name}.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")


class IceCreamStand(Restaurant):
    """A Class to represent a Ice Cream Stand."""

    def __init__(self, res_name, cuisine_type=None):
        """
        Initializing the attributes if Restaurant instance and
        IceCreamStand itself.
        """
        super().__init__(res_name, cuisine_type)
        self.flavors = []

    def add_flavors(self, *flavor):
        if flavor:
            for each in flavor:
                self.flavors.append(each)
        else:
            pass

    def get_flavors(self):
        print("\nWe've these flavors:")
        for flavor in self.flavors:
            print(f"\t{flavor.title()}")
