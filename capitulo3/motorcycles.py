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