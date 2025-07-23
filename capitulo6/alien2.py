#diccionarios, que representan un alien
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

#lista de diccionarios
aliens = [alien_0,alien_1,alien_2]
#iterar lista
for alien in aliens:
    print(alien)
print("==================")
#lista vacia de alients
aliens = []

#hacer 30 aliens verdes
for alien_number in range(30):#numero de veces que se itera lo siguiente:
    new_alien = {'color': 'green','points': 5,'speed':'slow'}#descripcion/creacion de alien
    aliens.append(new_alien)#agregar a lista vacia
#cambiar color de los 3 primeros elementos 
for alien in aliens [:3]:#iteracion 
    if alien['color'] == 'green':#condicion para el cambio
        alien['color'] = 'yellow'
        alien['points'] = 'medium'
        alien['speed'] = 10
    elif alien['color'] == 'yellow':#segunda condicion
        alien['color'] = 'red'
        alien['points'] = 'fast'
        alien['speed'] = 15

 #mostrar 5 los primeros 5 elementos de la lista vacia
for alien in aliens [:5]:
    print(alien)
print('...')
#mostrar los aliens que se han creado
print(f"numero total de aliens: {len(aliens)}")
