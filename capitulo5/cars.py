#lista de autos
cars = ['audi', 'bmw', 'subaru', 'toyota']
#mostrar en pantalla bmw con funcion titulo
print("mostrar en mayusculas elemento bmw sino mostrar elementos en letra capital:")
for car in cars:
    if car == 'bmw':#condicional si el valor es igual a, operador de igualdad
        print(car.upper())#accion
    else:#sin condicional no es el valor igual a entonces haz otra cosa
        print(car.title())
