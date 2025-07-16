# Crear una lista de números del 1 al 9 usando la función range()
numbers = list(range(1, 10))

# Recorrer cada número de la lista
for number in numbers:
    # Comprobar si el número es 1, ya que su forma ordinal termina en 'st'
    if number == 1:
        print(f"{number}st")
    # Comprobar si el número es 2, que termina en 'nd'
    elif number == 2:
        print(f"{number}nd")
    # Comprobar si el número es 3, que termina en 'rd'
    elif number == 3:
        print(f"{number}rd")
    # Para todos los demás números (4 en adelante), se usa 'th'
    else:
        print(f"{number}th")