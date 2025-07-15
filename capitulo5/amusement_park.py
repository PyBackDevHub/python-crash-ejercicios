# Edad de la persona
age = 75

# Primera versión: impresión directa del costo según la edad
# Condiciones de pago para el museo
if age < 4:  # Personas menores de 4 años entran gratis
    print("Your admission cost is $0.")
elif age < 18:  # Personas menores de 18 años pagan $25
    print("Your admission cost is $25.")
else:  # Personas de 18 años o más pagan $40
    print("Your admission cost is $40.")

print("============")  # Separador visual en la salida

# Segunda versión: asignación del precio a una variable antes de imprimir
age = 17  # Nueva edad para evaluar

# Determinación del costo de entrada según la edad
if age < 4:  # Menores de 4 años
    price = 0
elif age < 18:  # Menores de 18 años
    price = 25
elif age < 65:  # Adultos entre 18 y 64 años (precio completo)
    price = 40
else:  # Adultos mayores de 65 años (también $40, aunque podría haber descuento)
    price = 40

# Mostrar el costo final de entrada
print(f"Your admission cost is ${price}.")