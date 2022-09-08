from modules import py_vehicles as vehicles

kaskamovel = vehicles.EletricCar('Kask', 'Kaskavel', 2022, 100)

kaskamovel.battery.describe()
kaskamovel.get_descriptive_name()

print("\nDischarging 10kW")
kaskamovel.battery.discharging_battery(10)
kaskamovel.battery.describe()

print("\nDischarging 40kW")
kaskamovel.battery.discharging_battery(40)
kaskamovel.battery.describe()

print("\nCharging 25kW")
kaskamovel.battery.charge_battery(25)
kaskamovel.battery.describe()
