# Creamos un diccionario llamado 'user_info' que almacena información sobre una persona
user_info = {
    'first_name': 'hitman',   # Primer nombre
    'last_name': 'hart',      # Apellido
    'age': 99,                # Edad
    'city': 'okiwana',        # Ciudad en la que vive
}

# Recorremos el diccionario usando un bucle for
# 'key' representa la clave (por ejemplo, 'first_name')
# 'value' representa el valor asociado a esa clave (por ejemplo, 'hitman')
for key, value in user_info.items():
    # Imprimimos solo el valor de cada par clave-valor
    print(value)
