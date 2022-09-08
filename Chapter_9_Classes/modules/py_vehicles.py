"""This module should be used to represent any vehicle."""
from modules import py_battery


class Car:
    """Represents a car."""

    def __init__(self, make, model, year):
        """Initializes car attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 50

    def show_gas_tank(self):
        print(f"Fuel: {self.gas_tank}L")

    def empty_gas_tank(self, liters):
        self.gas_tank -= liters

    def fill_gas_tank(self, liters):
        self.gas_tank += liters

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

    def __init__(self, make, model, year, battery_size=10):
        """
        Initialize the attributes of parent class.
        Then initialize attributes specific to an eletric car.

        @battery_capacity: must be defined in killowatts.
        """
        super().__init__(make, model, year)
        self.battery = py_battery.Battery(battery_size)

    def fill_gas_tank(self, liters):
        pass

    def show_gas_tank(self):
        pass

    def empty_gas_tank(self, liters):
        pass
