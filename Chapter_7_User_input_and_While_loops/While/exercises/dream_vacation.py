responses = {}
active = True
prompt = "If you could visit one place in the world, where would you go?\n> "


while active:
    # Asking user's name and question.
    inp_name = input("What's your name?\n> ")
    inp_response = input(prompt)

    # Filling the dictionary
    responses[inp_name] = inp_response

    repeat = input("Will other person respond the question? (yes/no)\n> ")
    if repeat != 'yes':
        active = False

print("----- Results -----")
for name, response in responses.items():
    print(f"{name.title()} would visit {response.title()}")
