# Diccionario que almacena los ríos más importantes de cada continente
rivers_by_continent = {
    'Africa': ['Nile', 'Congo', 'Niger'],
    'Asia': ['Yangtze', 'Ganges', 'Mekong'],
    'Europe': ['Danube', 'Volga', 'Rhine'],
    'North America': ['Mississippi', 'Missouri', 'Colorado'],
    'South America': ['Amazon', 'Paraná', 'Orinoco'],
    'Australia': ['Murray', 'Darling'],
    'Antarctica': ['Onyx']  # Único río importante en la Antártida, estacional
}

# 1. Imprimir una oración sobre cada río y el continente al que pertenece
print("Rivers and the continents they run through:\n")
for continent, rivers in rivers_by_continent.items():
    for river in rivers:
        print(f"The {river} runs through {continent}.")

# 2. Imprimir la lista de todos los ríos
print("\nList of rivers:")
for rivers in rivers_by_continent.values():
    for river in rivers:
        print(f"- {river}")

# 3. Imprimir la lista de continentes (una vez cada uno)
print("\nList of continents:")
for continent in rivers_by_continent.keys():
    print(f"- {continent}")
