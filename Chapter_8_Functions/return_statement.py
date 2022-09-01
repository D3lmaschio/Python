# Middle is optional
def format_name(first, last, middle=''):
    """Returns full name, neatly formatted."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    
    return full_name.title()


print(format_name("matheus", "delmaschio"))
