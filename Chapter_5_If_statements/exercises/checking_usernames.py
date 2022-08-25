current_users = ['matheus', 'valdir', 'jose_carlos', 'admin', 'davi']
new_users = ['andre', 'julia', 'sofia', 'ana', 'joao', 'Davi']

cp_current_users = list(c_user.lower() for c_user in current_users)

for n_user in new_users:
    if n_user.lower() not in cp_current_users:
        print(f"The username {n_user} is available")
    else:
        print(
            f"The username {n_user} is already in use.\
            \nPlease enter a new username.")
