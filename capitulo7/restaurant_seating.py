#programa que pregunta al usuario por el número de personas que asistirán a una cena grupal
many_people = int(input("¿Cuántas personas asistirán la cena grupal?"))
#comprobar si hay espacio suficiente en la mesa
if many_people >= 8:
    print(f"\n tendran que esperar por una mesa")
else:
    print(f"\n la mesa esta lista pasen por favor")
