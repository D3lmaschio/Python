def show_messages(to_show):
    """
    Print the items of a list.
    """
    if to_show:
        for message in to_show:
            print(f"> {message.title()}\n")
    else:
        print("Nothing to show.")


messages = ['Hello World!', 'Meu nome é Matheus',
            'Python é legal', 'Meu time é uma bosta']

show_messages(messages)
