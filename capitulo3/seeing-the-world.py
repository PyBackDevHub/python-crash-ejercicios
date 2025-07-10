# Lista de lugares que me gustaría visitar (no en orden alfabético)
places = ['bangkok','sumatra','okinawa','ubekiztan','sahara']

# Imprimir la lista original
print("lista original:")
print(places)

# Imprimir la lista en orden alfabético sin modificar la original
print("\nLista en orden alfabético (con sorted):")
print(sorted(places))

# Verificar que la lista original no ha cambiado
print("\nLista después de usar sorted (debe ser igual a la original):")
print(places)

# Imprimir la lista en orden alfabético inverso sin modificar la original
print("\nLista en orden alfabético inverso (con sorted y reverse=True):")
print(sorted(places, reverse=True))

# Verificar nuevamente que la lista original no ha cambiado
print("\nLista final (sin cambios):")
print(places)

# Usar reverse() para invertir el orden de la lista
places.reverse()
print("Lista después de reverse():")
print(places)

# Usar reverse() nuevamente para volver al orden original
places.reverse()
print("\nLista después de reverse() otra vez (orden original restaurado):")
print(places)

# Usar sort() para ordenar la lista en orden alfabético (modifica la lista original)
places.sort()
print("\nLista ordenada alfabéticamente con sort():")
print(places)

# Usar sort() con reverse=True para ordenar en orden alfabético inverso
places.sort(reverse=True)
print("\nLista ordenada en orden alfabético inverso con sort(reverse=True):")
print(places)