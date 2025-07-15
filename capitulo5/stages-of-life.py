# Solicita al usuario que ingrese su edad y la convierte a entero
age = int(input("¿Cuál es tu edad? "))

# Verifica si la edad es menor que 2 años
if age < 2:
    print("Es un bebé")

# Verifica si la edad está entre 2 (inclusive) y 4 (exclusivo)
elif 2 <= age < 4:
    print("Es un infante")

# Verifica si la edad está entre 4 (inclusive) y 13 (exclusivo)
elif 4 <= age < 13:
    print("Es un niño")

# Verifica si la edad está entre 13 (inclusive) y 20 (exclusivo)
elif 13 <= age < 20:
    print("Es un adolescente")

# Verifica si la edad está entre 20 (inclusive) y 65 (exclusivo)
elif 20 <= age < 65:
    print("Es un adulto")

# Para cualquier otra edad (65 o más), se considera anciano
else:
    print("Es un anciano")