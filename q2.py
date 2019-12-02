cities = {
    'Karachi': {
        'country': 'Pakistan',
        'population': 61580,
        'Fact': 'Hospitatlity',
        },
    'Dehli': {
        'country': 'India',
        'population': 87678906,
        'Fact': 'Economy',
        },
    'Dhaka': {
        'country': 'Bangladesh',
        'population': 1003285,
        'Fact': 'Education',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    Facts= city_info['Fact'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print("  This country is very famous because of" + Facts + "." )
