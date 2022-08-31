prompt = "Enter 'quit' to end the program or 'reset' to start again.\n"
prompt += "Enter the toppings that you want:\n> "
toppings = []
topping = ""

while topping != 'quit':
    topping = str(input(prompt))

    if topping == 'quit':
        if len(toppings) > 0:
            print("\nYour toppings:")

            for top in toppings:
                print(f"\t{top.title()}")

        print("\nGoodbye!")

    elif topping == 'reset':
        toppings = []
        continue

    else:   
        print(f"\nAdding {topping.title()} topping to your pizza...\n")
        toppings.append(topping)
