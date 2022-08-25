user_names = ['matheus', 'valdir', 'jose_carlos', 'admin', 'davi']
login = ''

if login not in user_names:
    print("Please, enter a valid login.")
elif login == 'admin':
    print("Hello admin, would you like to see a status report?")
else:
    print(f"Hello, {login}!")
