# Diccionario que almacena los números favoritos de varias personas en forma de lista
# Cada persona tiene una lista de números favoritos

favorite_numbers = {
    'alice': [8, 7, 5],
    'bob': [42, 24, 12],
    'john': [35, 24, 77],
    'carol': [13, 31, 0],
    'dave': [3, 30, 96],
    'eve': [99, 9, 66]
}
# Imprimir cada persona con su número favorito,se usa .items() para obtener pares clave-valor, unpaking
for name, numbers in favorite_numbers.items():
    #mostrar el nombre de la persona y sus números favoritos
    print(f"{name.title()}'s favorite numbers are:")
    # Usar join para unir todos los números en una sola cadena
    #y convertir cada número a cadena, muestra de manera horizontal
    numebers_str = ', '.join([str(number) for number in numbers])#coberte cada número a cadena
    print(f"\t{numebers_str}")