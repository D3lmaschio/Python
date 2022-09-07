from modules.dog import Dog
from modules.restaurant import *

my_dog = Dog('Mel', 5)

print(f"My dog's name is {my_dog.name}")
print(f"{my_dog.name} is {my_dog.age} years old")
print("Sit down Mel!")
my_dog.sit()
print("Now roll over Mel!")
my_dog.roll_over()

ice_cream_stand = IceCreamStand('Delifruit')
ice_cream_stand.add_flavors('Chocolate', 'Baunilha', 'Limão', 'abacaxi')
ice_cream_stand.get_flavors()
