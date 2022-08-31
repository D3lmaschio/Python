responses = {}

polling_active = True

while polling_active:
    # Prompt for the person's name and response:
    name = input("\nWhat's your name:\n> ")
    response = input("\nWhat's the best anime for you?\n> ")

    # Adding key: name and value: response to the dictionary:
    responses[name] = response

    # Asking if the user want to quit:
    repeat = input(
        "\nWould you like to let another person respond? (yes / no)\n>  ")

    if repeat == 'no':
        polling_active = False

print("------- Results --------")

for name, response in responses.items():
    print(f"\n{name.title()} said that {response.title()} is the best anime.")
