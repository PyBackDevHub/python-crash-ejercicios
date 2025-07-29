#este es un ejemplo de bucle while con continue
# este código imprime los números impares del 1 al 9
# no imprime los números pares
currrent_number = 0# inicializar contador
while currrent_number < 10:# condición de parada
    # incrementar contador
    currrent_number +=1
    if currrent_number % 2 == 0:# condición de salto
        continue #salta el resto del bucle
    # imprimir el número actual
    print(currrent_number)