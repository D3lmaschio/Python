from telnetlib import BRK


prompt = "\nHello, I'm the parrot Jerry!"
prompt += "\nTell me something, and I will repeat it back  to you:\n"

message = ""
while True:
    if str.find(prompt, "You > ") == -1:
        prompt += "You > "
    else:
        prompt = "\nEnter 'quit' to end the program.\n"
        prompt += "You > "

    if message != 'quit':
        message = input(prompt)

    if message != 'quit':
        print(f"\nJerry the Parrot > {message}")
    else:
        print("Goodbye!")
        break
