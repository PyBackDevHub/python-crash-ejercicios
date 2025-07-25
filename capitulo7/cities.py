# este programa solicita al usuario que ingrese el nombre de una ciudad que ha visitado
# y muestra un mensaje con el nombre de la ciudad ingresada.
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True: #flag para continuar el bucle
    # Solicitar al usuario que ingrese el nombre de una ciudad
    city = input(prompt)# entrada del usuario

    if city == 'quit':# condicion de salida del bucle
        print("Gracias por participar.")
        break # salir del bucle
    else:# si no se ingresa 'quit'
        # Mostrar el nombre de la ciudad ingresada
        print(f"me gustaria ir a: {city.title()}")