cities = {
    'são paulo': {
        'country': 'brazil',
        'population': '12,033,000',
        'fact': 'São Paulo is carrying Brazil in his backs',
    },

    'new york': {
        'country': 'united states',
        'population': '8,038,000',
        'fact': "The city's original name was New Amsterdam",
    },

    'amsterdam': {
        'country': 'netherlands',
        'population': '821,752',
        'fact': 'The city has more canals than Venice',
    },
}

for city, about in cities.items():
    print(f"City: {city.title()}")

    for info, value in about.items():
        if info == 'country':
            country = value
        elif info == 'population':
            population = value
        elif info == 'fact':
            fact = value
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population.title()}")
    print(f"\tFact: {fact}")
