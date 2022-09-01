# The parameter to_send doesn't receive lists.
def send_messages(sent, *to_send):
    for message in to_send:
        sent.append(message)


sent_messages = []
send_messages(sent_messages,
              "Hello Darkens my old friend", "Python é legal",
              "Vou aprender Flask primeiro",
              "Vou terminar esse livro até o fim de semana.")

for messages in sent_messages:
    print(messages)
