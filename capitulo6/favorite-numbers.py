# Diccionario que almacena los números favoritos de varias personas
favorite_numbers = {
    'alice': 7,
    'bob': 42,
    'carol': 13,
    'dave': 3,
    'eve': 99
}

# Imprimir cada persona con su número favorito,se usa .items() para obtener pares clave-valor, unpaking
for name, language in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is, {language}")