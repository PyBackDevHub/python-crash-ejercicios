carro = 'subaru'

# Pruebas que evalúan a True (Verdadero)
print("¿El carro es igual a 'subaru'? Predigo que sí (True).")
print(carro == 'subaru')  # True porque carro es igual a 'subaru'

print("\n¿El carro es distinto de 'audi'? Predigo que sí (True).")
print(carro != 'audi')  # True porque carro no es igual a 'audi'

print("\n¿El carro en minúsculas es igual a 'subaru'? Predigo que sí (True).")
print(carro.lower() == 'subaru')  # True porque ya está en minúsculas

print("\n¿La longitud del nombre del carro es 6? Predigo que sí (True).")
print(len(carro) == 6)  # True porque 'subaru' tiene 6 letras

print("\n¿El nombre del carro comienza con 'sub'? Predigo que sí (True).")
print(carro.startswith('sub'))  # True porque comienza con 'sub'

# Pruebas que evalúan a False (Falso)
print("\n¿El carro es igual a 'audi'? Predigo que no (False).")
print(carro == 'audi')  # False porque carro no es 'audi'

print("\n¿El carro es igual a 'SUBARU'? Predigo que no (False).")
print(carro == 'SUBARU')  # False por diferencia en mayúsculas

print("\n¿El nombre del carro termina en 'xi'? Predigo que no (False).")
print(carro.endswith('xi'))  # False porque no termina en 'xi'

print("\n¿La longitud del nombre del carro es 5? Predigo que no (False).")
print(len(carro) == 5)  # False porque tiene 6 letras, no 5

print("\n¿La letra 'u' no está en el nombre del carro? Predigo que no (False).")
print('u' not in carro)  # False porque la 'u' sí está en 'subaru'
