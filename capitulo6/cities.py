#diccionario de ciudades con sus datos
# Cada ciudad tiene un país, población y un dato interesante
cities = {
    'tijuana':{
        'country': 'Mexico',
        'population': 2000000,
        'fact': 'Tijuana is known for its vibrant culture and nightlife.'
    },
    'new york':{
        'country': 'USA',
        'population': 8500000,
        'fact': 'New York City is known as "The Big Apple".'
    },
    'tokyo':{
        'country': 'Japan',
        'population': 14000000,
        'fact': 'Tokyo is the most populous city in the world.'
    },
    'paris':{
        'country': 'France',
        'population': 2200000,
        'fact': 'Paris is known as "The City of Light".'
    }
}
# Iterar sobre el diccionario para mostrar información de cada ciudad
for city, info in cities.items():
    # Mostrar el nombre de la ciudad
    print(f"\nciudad: {city.title()}")
    # Mostrar el país
    country = info['country']
    # Mostrar la población
    population = info['population']
    #mostrar un dato interesante
    fact = info['fact']
    #mostrar la información de la ciudad
    print(f"\tpais: {country.title()}")
    print(f"\tpoblacion: {population}")
    print(f"\tdato interesante: {fact}")
    #separa el bucle
    print("-" * 40)