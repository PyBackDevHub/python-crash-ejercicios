pets = ['perro', 'gato','perro','pez','gato','conejo','cat']
print(pets)
#condicional en la lista; mientras exista elemento gato en lista pets, eliminar gato y mostrar lista 
while 'gato' in pets:
    pets.remove('gato')
print(pets)

