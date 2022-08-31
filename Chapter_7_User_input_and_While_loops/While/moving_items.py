unconfirmed_users = ['Goku', 'Gohan', 'Piccolo', ]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

for user in confirmed_users:
    print(f"\nUser: {user.title()}\nStatus: Verified")

if unconfirmed_users:
    print("\nAre unconfirmed users in the system.")
else:
    print("\nAre no longer unconfirmed users in the system.")
