users = {#diccionario de usuarios
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'field': 'physics',
   },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'field': 'chemistry',
    },
}
#iteracion sobre el diccionario para mostrar los datos de cada usuario
#primero mostramos el nombre de usuario
for username, user_info in users.items():
    print(f"\nUsername : {username}")
    #mostramos el nombre completo
    full_name = f"{user_info['first']} {user_info['last']}"
    #mostrar la ubicacion
    location = user_info['location']
    #mostrar el campo de estudio
    field = user_info['field']
    #mostramos los datos del usuario
    print(f"\tFull name :{full_name.title()},")
    print(f"\tLocation :{location.title()}")
    print(f"\tField :{field.title()}")