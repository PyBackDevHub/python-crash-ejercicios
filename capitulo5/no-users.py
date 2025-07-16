# Lista de nombres de usuario (actualmente vacía)
usernames = []

# Verifica si la lista de usuarios está vacía
if not usernames:
    # Si la lista está vacía, muestra un mensaje indicando que se necesitan usuarios
    print("We need to find some users!")
else:
    # Si la lista no está vacía, recorre cada nombre de usuario en la lista
    for username in usernames:
        # Si el nombre de usuario es 'admin', muestra un mensaje especial
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            # Para cualquier otro usuario, muestra un mensaje de bienvenida genérico
            print(f"Bienvenido otra vez, {username}, inicia sesión.")