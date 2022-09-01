# This is a bad program.
def make_dict(key='', value=''):
    if key and value:
        return {key: value, }
    elif key and not value:
        return {key: ''}
    else:
        return {}


print("Programa para criar dicionários.\n")
print("Digite 'quit' para sair.")

user_dicts = []

while True:
    key = None
    value = None

    # Perguntando o tipo da KEY e qual será a KEY:
    inp_ktype = input("Enter the type of the key:"
                      " (int/float/str/list/tuple/set)\n> ")
    inp_key = input("\nEnter the key:\n> ")

    # Conferindo se o usuário digitou corretamente:
    turn_back = input(f"\nThe key is: {inp_key} and the type is: "
                      f">{inp_ktype}< ,is this correct? (yes/no)\n> ")

    if not (turn_back == 'yes'):
        continue

    inp_vtype = input("\nEnter the type of the value:"
                      " (bool/int/float/str/list/dict/tuple/set)\n> ")
    inp_value = input("\nEnter the value:\n> ")

    turn_back = input(f"The value is: {inp_value} and the type is: "
                      f">{inp_vtype}<, is this correct? (yes/no)\n> ")

    if not (turn_back == 'yes'):
        inp_vtype = input("\nEnter the type of the value:\n> ")
        inp_value = input("Enter the value:\n> ")

    print("\nMaking your dictionary...\n")

    if inp_ktype == 'int':
        key = int(inp_key)
    elif inp_ktype == 'float':
        key = float(inp_key)
    elif inp_ktype == 'list':
        key = list(inp_key)
    elif inp_ktype == 'tuple':
        key = tuple(inp_key)
    elif inp_ktype == 'set':
        key = set(inp_key)
    else:
        key = inp_key

    if inp_vtype == 'int':
        value = int(inp_value)
    elif inp_vtype == 'float':
        value = float(inp_value)
    elif inp_vtype == 'list':
        value = list(inp_value)
    elif inp_vtype == 'tuple':
        value = tuple(inp_value)
    elif inp_vtype == 'set':
        value = set(inp_value)
    else:
        value = inp_value

    created_dict = make_dict(key, value)

    print("Your dictionary is ready!")
    print(created_dict)

    repeat = input("\nDo you want do make another dictionary? (yes/no)\n> ")

    if not (repeat == 'yes'):
        user_dicts.append(created_dict)
        break
    else:
        user_dicts.append(created_dict)
