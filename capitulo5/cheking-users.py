# Lista de usuarios ya registrados en el sistema
current_users = ['admin2025', 'karla_xx', 'tecnogeek', 'coderLeo', 'noelia88']

# Lista de nuevos usuarios que quieren registrarse
new_users = ['coderLeo', 'noelia88', 'marco_dev', 'luisa2025', 'joseAdmin']

# Creamos una lista con los nombres actuales en minúsculas para hacer comparaciones insensibles a mayúsculas
current_users_lower = [user.lower() for user in current_users]

# Recorremos cada nuevo usuario en la lista new_users
for new_user in new_users:
    # Convertimos el nombre del nuevo usuario a minúsculas para comparación case-insensitive
    if new_user.lower() in current_users_lower:
        # Si el nombre ya existe (sin importar mayúsculas o minúsculas), avisamos que debe elegir otro
        print(f"{new_user} tiene que usar un nuevo usuario")
    else:
        # Si el nombre está disponible, indicamos que puede usarlo
        print(f"'{new_user}' usuario disponible")
