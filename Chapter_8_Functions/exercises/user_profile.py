def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything about the user
    using the given arguments.
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Matheus', 'Delmaschio',
                             location="Guarulhos, SP, Brasil",
                             age=19, company="Calvo")

print(user_profile)
