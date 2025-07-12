# Definimos una tupla llamada 'comidas' con 5 elementos
comidas = ("Hamburguesa", "Pizza", "Ensalada César", "Tacos al pastor", "Sopa de mariscos")

# Iteramos sobre la tupla para imprimir cada comida
print("Lista original de comidas:")
for comida in comidas:
    print(comida)

# Intento de modificar un elemento directamente en la tupla (esto daría error si se descomenta)
# comidas[1] = "Lasaña"  # ❌ Error: las tuplas son inmutables
# print(comidas)

# Convertimos la tupla a una lista para poder modificar sus elementos
comidas_lista = list(comidas)

# Modificamos algunos elementos de la lista
comidas_lista[1] = 'Lasaña'        # Reemplazamos "Pizza" por "Lasaña"
comidas_lista[2] = 'Sushi'         # Reemplazamos "Ensalada César" por "Sushi"
comidas_lista[-1] = 'Sopa Azteca'  # Reemplazamos el último elemento por "Sopa Azteca"

# Convertimos la lista modificada nuevamente a una tupla
comidas = tuple(comidas_lista)

# Imprimimos la nueva tupla modificada usando un bucle for
print("\nNueva tupla de comidas:")
for comida in comidas:
    print(comida)
