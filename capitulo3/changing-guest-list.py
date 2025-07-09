# Lista inicial de nombres invitados
nombres = ['Ana', 'Luis', 'Carlos', 'Marta', 'Sofía']

# Mensaje indicando que 'Marta' no asistirá a la cena
print("'marta' no asiste a la cena")

# Reemplaza el nombre en la posición 3 (cuarto elemento) por 'sayaman'
# Nota: Los índices empiezan en 0, por eso el índice 3 corresponde a 'Marta'
# También se podría usar índice negativo -2 para acceder a esta posición desde el final
nombres[3] = 'sayaman'

# Imprime la lista actualizada después del cambio
print(nombres)

# Imprime una línea en blanco (tabulación) para separar la salida
print("\t")

# Recorre cada nombre en la lista actualizada
for nombre in nombres:
    # Crea un mensaje de invitación personalizado para cada invitado
    mensaje = f"hola {nombre} eres invitado a la cena"
    # Imprime el mensaje de invitación
    print(mensaje)
