# Lista inicial de nombres invitados
nombres = ['kutsi', 'Ana', 'Luis', 'erlod', 'Carlos', 'sayaman', 'Sofía', 'yamada']

# Mensaje inicial indicando que solo hay espacio para dos invitados
print("solo se pueden invitar dos mas invitados")

# Mientras la lista tenga más de dos personas, eliminamos invitados uno a uno
while len(nombres) > 2:
    # Elimina el último invitado de la lista y lo guarda en 'eliminado'
    eliminado = nombres.pop()
    # Mensaje de disculpa para el invitado eliminado
    print(f"tu {eliminado}, no puedo invitarte a la cena.")

# Imprime una línea en blanco para separar secciones (tabulación)
print("\t")

# Mensajes para los dos invitados restantes en la lista
for name in nombres:
    invitado_restante = f"tu si eres invitado {name} a la cena"
    print(invitado_restante)

# Otra línea en blanco para separar secciones
print("\t")

# Imprime el título para la lista restante
print("lista restante:")
# Muestra la lista con los dos invitados que quedan
print(nombres)

# Línea en blanco para separar secciones
print("\t")

# Imprime el título para la lista eliminada completa
print("lista eliminada completa:")
# Vacía la lista 'nombres', eliminando todos los elementos restantes
del nombres[:]
# Imprime la lista vacía para confirmar que está limpia
print(nombres)
