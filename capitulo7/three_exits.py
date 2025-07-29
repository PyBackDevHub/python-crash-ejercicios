edad = int(input("ingresa tu edad o para salir '0'"))
while edad != 0:
    if edad < 3:
        print("usted entra gratis")
    elif 3 <= edad <=12 :
        print("usted paga $10")
    else:
        print("usted paga $15")

print("==========================================")

activo = True  # Variable de control

while activo:
    ingrediente = input("Agrega un ingrediente a la pizza (escribe 'quit' para salir): ")
    if ingrediente.lower() == "quit":
        activo = False  # Cambiamos la variable para salir del ciclo
    else:
        print(f"Has agregado {ingrediente} a tu pizza.")
print("==========================================")
while True:  # Bucle infinito
    ingrediente = input("Agrega un ingrediente a la pizza (escribe 'quit' para salir): ")
    if ingrediente.lower() == "quit":
        break  # Salimos inmediatamente del ciclo
    print(f"Has agregado {ingrediente} a tu pizza.")

