#tupla se separan por coma y se usan parentesis normal
dimensions = (200,50)
#mostrar elementos individualmente mediante el indice
print(dimensions[0])
print(dimensions[1])

#no se pueden cambiar los elementos pero si se pueden reasignar nuevos valores
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)