ingredientes = []
while True:
    elemento= input("agregar elementos a la pizza presiona 'quit' para salir")
    if elemento.lower() == 'quit':
        break
    else:
        ingredientes.append(elemento)
        print(f"haz agregado {elemento} a tu pizza")