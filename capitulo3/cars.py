# Definición de una lista de marcas de automóviles
cars = ['bmw', 'audi', 'toyota', 'subaru']

# Mostrar la lista original sin ordenar
print("Lista sin ordenar:")
print(cars)
print("\t")

# Ordenamiento permanente de la lista usando el método sort()
# Orden ascendente (de la A a la Z)
cars.sort()
print("Orden ascendente de la lista con el método .sort():")
print(cars)
print("\t")

# Ordenamiento permanente en orden descendente (de la Z a la A)
cars.sort(reverse=True)
print("Orden descendente de la lista con el método .sort(reverse=True):")
print(cars)
print("================================================")

# Mostrar la lista actual (ya ordenada en forma descendente)
print("Esta es la lista original después del ordenamiento descendente:")
print(cars)

# Aplicar ordenamiento temporal con la función sorted()
# La función sorted() devuelve una nueva lista ordenada, sin modificar la original
print("\nEsta es la lista ordenada temporalmente (orden ascendente):")
print(sorted(cars))

# Verificar que la lista original no se ha modificado
print("\nEsta es la lista original nuevamente (sin cambios):")
print(cars)
print("================================================")

# Definición de una lista de marcas de automóviles
cars = ['bmw', 'audi', 'toyota', 'subaru']

# Mostrar la lista original
print("Lista original:")
print(cars)
print("\t")

# Uso del método reverse()
# El método .reverse() invierte el orden de los elementos de la lista de forma permanente,
# es decir, modifica directamente la lista original, pero NO la ordena alfabéticamente.
print("Lista después de aplicar el método .reverse():")
cars.reverse()
print(cars)

# la funcion len() para saber la longitud de la lista
print("muesta numero de elementos de la lista:")
print(len(cars))