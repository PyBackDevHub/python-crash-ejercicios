# Se crea una lista vacía llamada 'cubo' que almacenará los cubos de los números
cubo = []

# Se recorre un rango de números del 1 al 9 (el 10 no se incluye)
for value in range(1, 10):
    # Se calcula el cubo del número actual (value ** 3) y se agrega a la lista 'cubo'
    cubo.append(value ** 3)

# Se imprime la lista completa de cubos
print(cubo)
