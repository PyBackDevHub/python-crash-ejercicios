#diccionario vacio
respuestas = {}
#establecer una bandera indicq que el sondeo esta activado
sondeo_active = True
while sondeo_active:
#pide input al usario
    nombre = input("\ncual es tu nombre? ")
    respuesta = input("cual montaña le gustaria escalar algun dia?: ")
#guardar la respuesta en el diccionario
    respuestas[nombre] = respuesta

#encontrar si alguien mas va a tomar el sondeo
    repetir = input("quiere que otra persona responda? (si/no) ")
    if repetir == 'no':
        sondeo_active = False

# sondeo compleatado, mostrar los resultados
print("\n ---- resultados sondeo ----")
#iteracion
for nombre,respuesta in respuestas.items():
    print(f"{nombre} te gustaria escalar {respuesta}.")