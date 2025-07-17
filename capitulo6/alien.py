# Diccinario, es key value pair o pares de llave o valor
alien_0 = {'color': 'green', 'points': 5}
#mostrar el valor utilizando la llave
print("accesando al valor asociado de cada par desde la llave:")
print(alien_0['color'])
print(alien_0['points'])
#ejemplo de puntos ganados por matar un alien 
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
print("=====")
#ejemplo de agregar dos piezas de informacion
print("mostrar alien en posicion particular de la pantalla:")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print("==================")
# Empezar con diccionario vacio
alien_0 = {}

#valores diccionario
alien_0['color'] = 'green'
alien_0['points'] = '5'

print("mostrar diccionario desde pantalla vacia:")
print(alien_0)
#modificacion de diccionario
print("==============")
print("actualizacion de color:")
alien_0['color'] = 'black'
print(f"The alien is {alien_0['color']}.")

print("\nactualizacion de color:")
alien_0['color'] = 'purple'
print(f"The alien is {alien_0['color']}.")
#dar seguimiento a la posicion del alien
print("==============")
alien_0 = {'x_position': '0','y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

#mover el alien a la derecha
#determinar que tan lejos se mueve el alien basado en su actual velocidad
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #ese debe ser un alien rapido
    x_increment = 3
#la nueva posicion es la vieja posicion mas el incremento
alien_0['x_position'] = {alien_0['x_position'] + x_increment}

print(f"nueva posicion: {alien_0['x_position']}")

#para borrar un par del diccionario
print("==============")
print(" se usa del mas la llave para borrar:")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)