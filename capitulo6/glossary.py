# Diccionario que representa un glosario de términos de programación
glossary = {
    'variable': 'A name that stores a value which can change during program execution.',
    'function': 'A block of code that performs a specific task and can be reused.',
    'loop': 'A control structure used to repeat a block of code multiple times.',
    'dictionary': 'A collection of key-value pairs, where each key is unique.',
    'string': 'A sequence of characters used to represent text.'
}

# Imprimir cada palabra con su definición, con formato limpio
for word, meaning in glossary.items():
    print(f"{word.title()}:\n  {meaning}\n")
