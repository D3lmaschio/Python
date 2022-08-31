prompt = "Enter 'quit' to end the program.\n"
prompt += "Enter your age:\n> "

while True:
    inp = input(prompt)

    if inp.isnumeric():
        inp = int(inp)

    if inp == 'quit':
        print("Goodbye!")
        break

    if inp < 3:
        print("Your movie ticket is free!\n")
        continue
    elif (inp > 3) and (inp <= 12):
        print("Your movie ticket is $10\n")
        continue
    elif inp > 12:
        print("Your movie ticket is $15\n")
        continue
