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
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll odometer back!")

    def get_descriptive_name(self):
        """Return a neatly formatted description of the instance."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """Print a statement showing the car's milleage."""
        print(f"This car has {self.odometer_reading} miles on it.")


class EletricCar(Car):
    """Representation of a car specific an eletric vehicle."""

    def __init__(self, make, model, year):
        """
        Initialize the attributes of parent class.
        Then initialize attributes specific to an eletric car.
        """
        super().__init__(make, model, year)
        self.battery = 75

    def decrease_battery(self, used_energy):
        """Remove the given amount of the battery."""
        self.battery -= used_energy

    def increase_battery(self, charge):
        """Add the given amount to the battery."""
        self.battery += charge

    def get_battery(self):
        """Print a statement showing the battery's percentage."""
        print(f"{self.battery}%")


tesla = EletricCar('tesla', 'tesla s', 2019)
print(tesla.get_descriptive_name())
tesla.get_battery()
tesla.decrease_battery(5)
tesla.get_battery()
tesla.increase_battery(10)
tesla.get_battery()

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
