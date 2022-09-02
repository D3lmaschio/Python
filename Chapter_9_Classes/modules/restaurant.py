class Restaurant:

    def __init__(self, res_name, cuisine_type):
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


my_restaurant_0 = Restaurant("Delmaschio's", "Italian")
my_restaurant_1 = Restaurant("French Fries", "French")
my_restaurant_2 = Restaurant("Bom Prato", "Brasilian")

my_restaurant_0.describe_restaurant()
my_restaurant_0.open_restaurant()

my_restaurant_1.describe_restaurant()
my_restaurant_1.open_restaurant()

my_restaurant_2.describe_restaurant()
my_restaurant_2.open_restaurant()
