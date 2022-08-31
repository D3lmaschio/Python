prompt = "Enter 'quit' to end the program or 'reset' to start again.\n"
prompt += "Enter the toppings that you want:\n> "
toppings = []

while True:
    topping = str(input(prompt))

    if topping == 'quit':
        if len(toppings) > 0:
            print("\nYour toppings:")

            for top in toppings:
                print(f"\t{top.title()}")

        print("\nGoodbye!")
        break
    elif topping == 'reset':
        toppings = []
        continue

    print(f"\nAdding {topping.title()} topping to your pizza...\n")
    toppings.append(topping)
