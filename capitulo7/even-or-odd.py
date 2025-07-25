#mostrar si un numero es par o impar
# Ejemplo de uso de int() con input()
number = input("Introduce un número: ")
number = int(number)  # Convertir la entrada a un número entero
# Verificar si el número es par o impar
if number % 2 == 0:# Verifica si el residuo de la división por 2 es cero
    print(f"\n{number} es un número par.")
else:
    print(f"\n{number} es un número impar.") 