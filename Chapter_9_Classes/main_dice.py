from modules.py_dice import Dice

inp_sides = int(input("Creating the dice...\n"
                      "How many sides the dice must have?\n> "))
dice = Dice(inp_sides)

while True:
    inp_ifroll = input("\nRoll dice? (yes/no)\n> ")

    if inp_ifroll.strip() != 'no':
        inp_times = input("How many times?"
                          " (press ENTER if you want to do it once.)\n> ")

        if inp_times.isalnum():
            times = int(inp_times)
        else:
            times = 1

        result = dice.roll_dice(times)
        if times > 1:
            print("\nResult of {time}rolls:")
            for time in times:
                print(f"\tRoll {time}: {result}")
        elif times > 0:
            print(f"Roll result: {result}")
        else:
            print(0)
    else:
        print("\nBye\n")
        break
