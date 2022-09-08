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
        """Returns the remaining power of the battery in percent."""
        remaining_power = (self.battery_charge
                           / (self.MAX_BATTERY_CAPACITY / 100.0))
        return remaining_power

    def describe(self):
        """Print a statement describing status of the battery."""
        print(f"Battery:\n\tMax Capacity:{self.MAX_BATTERY_CAPACITY}kW"
              f"\n\tCharge remaining:{self.get_remaining_power():.0f}%")
