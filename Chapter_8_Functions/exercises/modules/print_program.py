def print_list(*args):
    """
    Print items from a list.
    """
    if args:
        for arg in args:
            print(arg)
    else:
        return None


def print_dict(**kwargs):
    """
    Print a neatly formatted dictionary.
    """
    if kwargs:
        for key, value in kwargs:
            print(f"{key}: {value}")
    else:
        return None
