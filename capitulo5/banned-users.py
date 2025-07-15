# Lista de usuarios bloqueados o prohibidos para comentar
banned_users = ['andrew', 'carolina', 'david']

# Nombre del usuario actual
user = 'marie'

# Verificación: si el usuario NO está en la lista de bloqueados, se le permite comentar
# IMPORTANTE: usamos 'not in' para verificar que 'user' no esté en la lista
if user not in banned_users:
    print(f"{user.title()}, puedes publicar una respuesta si lo deseas.")
