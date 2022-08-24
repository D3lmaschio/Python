my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
friend_foods = my_foods[:]

my_foods.append("lasagna")
friend_foods.append("shrimp")


for food in my_foods:
    print(f"I like {food.title()}")

for food in friend_foods:
    print(f"My friends like {food.title()}")
    