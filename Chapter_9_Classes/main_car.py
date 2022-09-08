from modules import vehicles

kaskamovel = vehicles.EletricCar('Kask', 'Kaskavel', 2022, 100)

kaskamovel.describe()
kaskamovel.get_descriptive_name()

print("\nDischarging 10kW")
kaskamovel.discharging_battery(10)
kaskamovel.get_remaining_power()

print("\nDischarging 40kW")
kaskamovel.discharging_battery(40)
kaskamovel.get_remaining_power()

print("\nCharging 25kW")
kaskamovel.charge_battery(25)
kaskamovel.get_remaining_power()
