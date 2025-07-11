# Lista de nombres de magos
magicians = ['alice', 'david', 'carolina']

# Imprime un mensaje indicando que se mostrará la lista original (sin iterar)
print("\nLista de elementos sin iterar o lista original:")
print(magicians)

# Bucle for para iterar sobre cada elemento de la lista y mostrar mensajes personalizados
print("\nElementos dentro de la lista 'magicians' después de iterar:")
for magician in magicians:
    # Se imprime un mensaje felicitando al mago por un gran truco
    print(f"{magician.title()}, that was a great trick!")
    
    # Se imprime un mensaje indicando entusiasmo por el próximo truco
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Mensaje final después de que el bucle ha terminado
print("Thank you, everyone. That was a great magic show!")

