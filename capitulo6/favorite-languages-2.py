favorite_languages = {
    'jen': ['python','rust'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
#iteracion sobre el diccionario
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")#muesta el nombre con la primera letra en mayuscula
    for language in languages:
        print(f"\t{language.title() }")# muestra el lenguaje con la primera letra en mayuscula
# muestra el nombre y los lenguajes favoritos de cada persona