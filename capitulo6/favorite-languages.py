# Diccionario que almacena los lenguajes de programación favoritos de varias personas
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# Accede al lenguaje favorito de Sarah y lo convierte a mayúscula inicial
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# ====================

# Ejemplo del uso de get() para obtener un valor de un diccionario de forma segura
print("====================")
alien_0 = {'color': 'green', 'speed': 'slow'}

# Se intenta obtener el valor asociado con la clave 'points'
# Si no existe, se devuelve el mensaje predeterminado
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# =================

# Mostrar todos los lenguajes mencionados, incluyendo repeticiones
print("=================")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    # Se muestra cada lenguaje con la primera letra en mayúscula
    print(language.title())

# ============

# Mostrar solo los lenguajes únicos usando un conjunto (set)
print("============")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    # Se eliminan duplicados al convertir los valores a un set
    print(language.title())
