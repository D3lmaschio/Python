def make_car(manufacturer, model, **kwargs):
    """
    Create a dictionary of a car with all args.
    """
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs


car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
