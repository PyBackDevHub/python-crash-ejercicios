# Lista de nombres de usuario
usernames = ['admin', 'admin123', 'superadmin', 'admin_user', 'admin2025', 'administrator']

# Itera sobre cada nombre de usuario en la lista
for username in usernames:
    # Si el usuario actual es exactamente 'admin', imprime un mensaje especial
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        # Para cualquier otro usuario, imprime un mensaje de bienvenida estándar
        print(f"Bienvenido otra vez, {username}, inicia sesión.")
