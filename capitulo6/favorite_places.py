#diccinario con varios usuarios --key: nombre de usuario y valor: lugares favoritos
#cada usuario tiene una lista de lugares favoritos
favorite_places = {
    'alice': ['paris', 'london', 'new york'],
    'bob': ['tokyo', 'berlin'],
    'charlie': ['sydney', 'cairo', 'mumbai'],
    'dave': ['rio de janeiro', 'cape town'],
    'eve': ['moscow', 'beijing', 'seoul']
}
#iteracion sobre el diccionario para mostrar los lugares favoritos de cada usuario
for username, places in favorite_places.items():
    #mostrar el nombre de usuario
    print(f"\nal usuario {username.title()} le gustan los siguientes lugares:")
    # Usar join para unir todos los lugares en una sola cadena usando una lista por comprensión
    #y convertir cada lugar a mayúscula, muestra de manera horizontal
    #y separarlos por comas
    lugares = ', '.join([place.title() for place in places])
    print(f"\t{lugares}")
    #otra manera de mostrar los lugares favoritos esta en forma de lista vertical
    for place in places:
    #mostrar cada lugar favorito
        print(f"\t- {place.title()}")
         #separar cada usuario con una linea
    print("-" * 20)