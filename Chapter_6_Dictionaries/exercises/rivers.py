countries = {
    'egipt': 'nile',
    'brazil': 'amazonas',
    'united states': 'mississipi',
}

for country in countries:
    river = countries.get(country)
    print(f"The {river.title()} runs through {country.title()}")
