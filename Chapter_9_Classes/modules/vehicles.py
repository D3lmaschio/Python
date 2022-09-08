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


class Battery:
    """Representation of a battery."""

    def __init__(self, kilowatts=0.0):
        """
        Initializes the attributes for parent class battery.
        @const MAX_CAPACITY is the limit of the battery, is
        defined in the instantation of the class.
        """
        if kilowatts >= 0.0:
            self.MAX_BATTERY_CAPACITY = kilowatts  # CONSTANT
            self.battery_charge = self.MAX_BATTERY_CAPACITY
        else:
            self.MAX_BATTERY_CAPACITY = None
            self.battery_charge = self.MAX_BATTERY_CAPACITY

    def charge_battery(self, kwh):
        """Increment the given amount(kWh) to the battery instance."""
        if kwh >= 0.0:
            self.battery_charge += kwh

    def discharging_battery(self, kwh):
        """Decrement the given amount(kWh) of the battery instance."""
        if kwh >= 0.0:
            self.battery_charge -= kwh

    def get_remaining_power(self):
        """Print out the remaining power of the battery in percent."""
        remaining_power = (self.battery_charge
                           / (self.MAX_BATTERY_CAPACITY / 100.0))
        return remaining_power

    def describe(self):
        """Print a statement describing status of the battery."""
        print(f"Battery:\n\tMax Capacity:{self.MAX_BATTERY_CAPACITY}"
              f"\n\tCharge remaining:{self.get_remaining_power()}")


class EletricCar(Car, Battery):
    """Representation of a car specific an eletric vehicle."""

    def __init__(self, make, model, year, battery_capacity):
        """
        Initialize the attributes of parent class.
        Then initialize attributes specific to an eletric car.

        @battery_capacity: must be defined in killowatts.
        """
        super(Car).__init__(make, model, year)
        super(Battery).__init__(battery_capacity)

    def fill_gas_tank(self, liters):
        pass

    def show_gas_tank(self):
        pass

    def empty_gas_tank(self, liters):
        pass
