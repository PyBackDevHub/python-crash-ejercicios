# Lista de ingredientes que el cliente ha solicitado para su pizza
requested_toppings = ['mushrooms', 'extra cheese']

# Verificar si cada ingrediente específico está en la lista y agregarlo si corresponde

if 'mushrooms' in requested_toppings:  # Si se solicitó champiñones
    print("Adding mushrooms.")

if 'pepperoni' in requested_toppings:  # Si se solicitó pepperoni
    print("Adding pepperoni.")

if 'extra cheese' in requested_toppings:  # Si se solicitó queso extra
    print("Adding extra cheese.")

# Mensaje final indicando que se ha terminado de preparar la pizza
print("\nFinished making your pizza!")

print("===============")
print("\nversion mejorada")
# Lista de ingredientes que el restaurante tiene disponibles
ingredientes_disponibles = ['champiñones', 'pepperoni', 'queso extra', 'aceitunas', 'cebolla']

# Solicitar al usuario que escriba los ingredientes deseados
entrada = input("Ingrese los ingredientes que desea en su pizza, separados por comas: ")

# Convertir la entrada en una lista y eliminar espacios adicionales
ingredientes_solicitados = [ingrediente.strip().lower() for ingrediente in entrada.split(',')]

# Recorrer cada ingrediente solicitado por el usuario
for ingrediente in ingredientes_solicitados:
    if ingrediente in ingredientes_disponibles:
        print(f"Añadiendo {ingrediente}.")
    else:
        print(f"Lo siento, no tenemos {ingrediente}.")

# Mensaje final de confirmación
print("\n¡Pizza terminada! Gracias por su pedido.")
