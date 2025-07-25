#pide un mumero al usuario y muestra si es mutliplo de 10
numero = int(input("introduce un numero para saber si es multiplo de 10: "))
#comprobar si es multiplo de 10
if numero % 10 == 0:
    print(f"\n{numero} es muiltiplo de 10")
else:
    print(f"\n{numero} no es muiltiplo de 10")