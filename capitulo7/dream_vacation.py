#lugar que me gustaria visitar ejercicio
#diccionario vacio
lugares = {}
#indicar que el sondeo esta activo
polling_active = True

while polling_active:
    #introducir nombre y lugar
    name = input("nombre por favor")
    lugar = input("lugar a visitar")
#guardar informacion de input en el diccionario vacio
    lugares[name] = lugar
#averiguar si alguien mas va a ingresar datos
repetir = input("alguien mas para agregar? si/no")
if repetir == 'no':
    polling_active = False
#mostrar datos
print("\n mostrar datos")
for name, lugar in lugares.items():
    print(f"{name} gustaria ir {lugar}")