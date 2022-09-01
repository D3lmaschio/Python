def send(to_send, sent):
    if to_send:
        while to_send:
            sent.append(to_send.pop())

            if not to_send:
                for sent_message in sent:
                    print(f'\n> Sent: "{sent_message}"')

    else:
        print("Nothing to show.")


sent_messages = []
messages = ['Hello World!', 'Meu nome é Matheus',
            'Python é legal', 'Meu time é uma bosta']

send(messages[:], sent_messages)

print(messages)
print(sent_messages)
