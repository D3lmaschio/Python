class Restaurant:

    def __init__(self, res_name, cuisine_type):
        """
        Intialize the class with restaurant name and cuisine type 
        as arguments.
        """
        self.name = res_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

    def describe_restaurant(self):
        print(f"The {self.cuisine_type} restaurant {self.name}.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

    def get_served(self):
        print(f"{self.name} restaurant has served "
              f"{self.number_served} consumers today.")


restaurant = Restaurant("Delmaschio's", 'Italian')
restaurant.get_served()
restaurant.number_served = 100
restaurant.get_served()
restaurant.set_number_served(10)
restaurant.get_served()
restaurant.increment_number_served(100)
restaurant.get_served()
