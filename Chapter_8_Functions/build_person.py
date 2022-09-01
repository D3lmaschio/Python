def build_person(first, last, age=None):
    """Returns a dictionary of information about a person."""
    if age:
        person = {'first': first, 'last': last, 'age': age}
    else:
        person = {'first': first, 'last': last, }

    return person


me = build_person("Matheus", "Rubens", 19)
print(me)
