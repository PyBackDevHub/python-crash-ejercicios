# Lista inicial de nombres invitados
nombres = ['Ana', 'Luis', 'Carlos', 'sayaman', 'Sofía']

# Imprime la lista original de nombres
print(nombres)

# Inserta 'kutsi' al inicio de la lista (posición 0)
nombres.insert(0, 'kutsi')

# Inserta 'erlod' en la posición 3 de la lista (desplazando los elementos hacia la derecha)
nombres.insert(3, 'erlod')

# Añade 'yamada' al final de la lista
nombres.append('yamada')

# Recorre cada nombre en la lista actualizada
for name in nombres:
    # Crea un mensaje de invitación personalizado para cada nombre
    invitation = f"hola {name} esta es tu invitacion de la cena"
    # Imprime el mensaje de invitación
    print(invitation)
