#crea lista people con 3 diccionarios que son 3 personas con sus datos
people = [
    {
    'first_name': 'hitman',   # Primer nombre
    'last_name': 'hart',      # Apellido
    'age': 99,                # Edad
    'city': 'okiwana',        # Ciudad en la que vive
    },
    {
    'first_name': 'james',    # Primer nombre
    'last_name': 'bond',      # Apellido
    'age': 40,                # Edad
    'city': 'londres',        # Ciudad en la que vive
    },
    {
    'first_name': 'jane',     # Primer nombre
    'last_name': 'doe',       # Apellido
    'age': 30,                # Edad
    'city': 'new york',       # Ciudad en la que vive
    },

]
# Recorremos la lista de personas usando un bucle for
for person in people:
    #imprimir el nombre completo de cada persona
    full_name = f"{person['first_name']}, {person['last_name']}"
    age = person['age']  # Edad de la persona
    city = person['city']  # Ciudad de la persona

    #mostras datos de cada persona
    print(full_name)
    print(f"\tAge: {age}")
    print(f"\tCity: {city.title()}")
    #separar cada persona con una linea
    print("-" * 20)