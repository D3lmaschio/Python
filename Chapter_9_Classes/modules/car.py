class Car:
    """Represents a car."""

    def __init__(self, make, model, year):
        """Initializes car attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def update_odometer(self, mileage):
        """
        Set the odometer reading with to given mileage.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amout to the odometer reading."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll odometer back!")

    def get_descriptive_name(self):
        """Return a neatly formatted description of the instance."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """Print a statement showings the car's milleage."""
        print(f"This car has {self.odometer_reading} miles on it.")


my_car = Car('Ford', 'Camaro', '2012')
print(my_car.get_descriptive_name())
my_car.read_odometer()

# Simplest way to modify a instance attribute is \
# setting directly the attribute:
my_car.odometer_reading = 23
my_car.read_odometer()

# Modifying an Attribute’s Value Through a Method:
print("\nTrying to roll odometer back:")
my_car.update_odometer(10)
my_car.read_odometer()

# Incrementing an Attribute’s Value Through a Method:
print("\nIncrementing the odometer:")
my_car.increment_odometer(10)
my_car.read_odometer()

print("\nTrying to roll odometer back.")
my_car.increment_odometer(-10)
my_car.read_odometer()
