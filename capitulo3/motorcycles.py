#lista de motocicletas
print("lista de marcas de motocicletas:")
motorcycles = ['honda','yamaha','suzuki']
#imprir lista
print(motorcycles)
print("\t")
print("\t")
#forma de modificar elemento de la lista
print("primer elemento modificado de la lista:")
motorcycles[0] = 'ducati'
print(motorcycles)
print("\t")
#anexar un elemento nuevo a la lista
print("mostrar lista con nuevo elemento,metodo anexar(.append()) agrega un elemento al final de la lista:")
motorcycles.append('ducati')
#imprimir lista modificada
print(motorcycles)
print("===============")
#lista vacia
motorcycles = []
#agregar elementos de manera individual al lista vacia
print("agregar elementos a la lista al final:")
motorcycles.append('honda')
motorcycles.append('yahama')
motorcycles.append('suzuki')
print(motorcycles)
print("\t")
motorcycles = ['honda','yamaha','suzuki']
#agregar elementos especificando en el indice en este caso en la primera posicion
print("agregar elementos especificando el indice de el nuevo elemento y el valor del mismo con metodo insertar(.insert()):")
motorcycles.insert(0,'ducati')
print(motorcycles)
print("\t")
#eliminar elementos de la lista con indice especifico y no usar mas
#del [:]elimina todos los elementos
print("borrar elemento con declaracion del(borrar) con indice 0 o primer elemento:")
del motorcycles[0]
print(motorcycles)
print("\t")
#eliminar ulitmo elemento de la lista y permite trabajar con el elemento borrado
print("metodo .pop() elimina ultimo elemento /dentro del parentesis poner el indice y permite trabajar con el mismo:")
popped_motorcycles = motorcycles.pop()
print(f"last motorcycle i owned was a {popped_motorcycles.title()}")
print("\t")
#remover elemento de la lista 
print("metodo .remove() elimina el primer elemento repedito de lista, se ocupa un for loop para eliminar mas del mismo: ")
too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n{too_expensive.title()} is too expensive for me")

