#lista de jugadores
players = ['charles', 'martina', 'michael', 'florence', 'eli']
#extraer sublista de los 3 primeros elementos o slicing
print("primeros 3 elementos:")
print(players[0:3])
#extraer sublista del segundo al cuarto elemento
print("\ndel segundo al cuarto elemento:")
print(players[1:4])
#extraer sublista de los 4 primeros elementos
print("\nprimeros 4 elementos:")
print(players[:4])
#extraer sublista de los ultimos 3 elementos
print("\nultimos 3 elementos:")
print(players[-3:])
#si agregas un tercer elemento paso: opcional, indica cada cuántos elementos se toman.
print("\ninicio,fin,paso:")
print(players[0:4:2])
#ciclo for a traves de un sub conjunto de elementos
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
