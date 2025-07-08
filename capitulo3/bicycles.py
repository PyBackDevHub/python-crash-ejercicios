"""
Script que muestra una lista de marcas de bicicletas.

demuestra como definir una lista en python y como imprimir su contenido
"""
#lista dentro de una variable
bicycles = ['trek','cannondale','redline','specialized']
#mostrar en pantalla 
print("muestra lista completa:")
print(bicycles)
print("\t")
#mostrar elemento 1 o primero de la lista
print("muestra primer elemento de la lista:")
print(bicycles[0])
print("\t")
#muestra primer elemento con la funcion titulo 
print("muestra elemento en formato titulo:")
print(bicycles[0].title())
print("\t")
#muestra elementos 2 y 4 de la lista
print("muestra elementos con indices 1 y 3:")
print(bicycles[1])
print(bicycles[3])
print("\t")
#muestra el ultimo elemento de la lista,especial del lenguaje,es mostrar la lista al reves del ultimo al primero, -2,-3...
print("muestra el elemento con indice -1, que es el ultimo elemento:")
print(bicycles[-1])
print("\t")
#mostrar mensaje con formato f-string,titulo
print("se muestra mensaje con formato f-string, titulo del primer elemento:")
message = f"my first bicycle was a {bicycles[0].title()}"
print(message)
print("\t")
#