# Asignamos el color del alien a la variable alien_colors
alien_colors = 'green'

# Comprobamos si el color del alien es 'green'
if alien_colors == "green":
    # Si es 'green', el jugador gana 5 puntos
    print("player earns 5 points")

# Si no es 'green', comprobamos si el color NO es 'yellow'
elif alien_colors != "yellow":
    # Si el color es diferente de 'yellow', el jugador gana 10 puntos
    # NOTA: Esta condición incluye 'red', pero también cualquier otro color que no sea 'yellow'
    print("player earns 10 points")

# Si ninguna de las condiciones anteriores se cumple, comprobamos si es 'red'
elif alien_colors == "red":
    # Este bloque nunca se ejecutará si el color es 'red' debido al orden de condiciones
    # porque 'red' ya cumple alien_colors != "yellow" en el bloque anterior
    print("player earns 15 points")
