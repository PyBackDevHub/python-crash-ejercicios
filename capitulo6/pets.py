#lista de mascotas con sus dueños
#cada mascota es un diccionario con el tipo de animal y el dueño
pets = [
    {'animal': 'perro', 
     'owner': 'Carlos'},
    {'animal': 'gato', 
     'owner': 'Ana'},
    {'animal': 'loro', 
     'owner': 'Luis'},
    {'animal': 'conejo', 
     'owner': 'María'},
    {'animal': 'pez', 
     'owner': 'Sofía'}
]
#iteracion sobre la lista de mascotas
for pet in pets:
    #mostrar el tipo de animal y su dueño
    animal = pet['animal']
    dueno =pet['owner']
    print(f"el dueño de {animal.title()} es {dueno.upper()}.")
    #separar cada mascota con una linea
    print("-" * 20)
