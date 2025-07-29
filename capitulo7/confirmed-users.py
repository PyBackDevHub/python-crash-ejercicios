#empezar con usariaos que necesitan ser verificados
# y una lista vacia que los mantiene como usuarios confirmados
usarios_inconfirmados = ['alice','brain','candence']
usuarios_confirmados = []#lista vacia par personas

#verificar cada usuario hasta que no hay mas inconformados
#mover cada usuario verificado dentro de la lista de usuarios confirmados
#condicional
while usarios_inconfirmados:
    usuario_actual = usarios_inconfirmados.pop()# elimina elementos de la lista confirmada, desde el final de la lista. metodo remove para seleccionar el indice a borrar

    print(f"verificado usuario: {usuario_actual.title()}") #muestra estado actual
    usuarios_confirmados.append(usuario_actual)#agrega a la lista vacia

#muestra todos los usuarios confirmados
print("\nlos siguientes usuarios han sido confoirmados")
#se itera la lista
for usuarios_confirmado in usuarios_confirmados:
    print(usuarios_confirmado.title())