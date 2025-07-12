# Lista original de pizzas favoritas
mi_pizza = [
    "Margarita",
    "Pepperoni",
    "Hawaiana",
    "Cuatro Quesos",
    "Vegetariana"
]

# Creamos una copia de la lista original para el amigo
amigo_pizza = mi_pizza[:]  # copia independiente usando slicing

# Agregamos una nueva pizza a la lista original
mi_pizza.append("Pizza al pesto")

# Agregamos una pizza diferente en una posición específica a la lista del amigo
amigo_pizza.insert(3, "Napolitana")

# Imprimir mensaje para la lista original
print("Mis pizzas favoritas son:")
# Usar un bucle for para imprimir cada pizza en la lista original
for pizza in mi_pizza:
    print(pizza)

print()  # línea en blanco para separar las listas

# Imprimir mensaje para la lista del amigo
print("Las pizzas favoritas de mi amigo son:")
# Usar un bucle for para imprimir cada pizza en la lista del amigo
for pizza in amigo_pizza:
    print(pizza)
