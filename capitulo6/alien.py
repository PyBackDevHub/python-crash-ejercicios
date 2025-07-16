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


