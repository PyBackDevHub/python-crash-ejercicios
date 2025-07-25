#como usar funcion int en funcion input
# Ejemplo de uso de int() con input()
heith = input("Introduce tu altura en cm: ")
heith = int(heith)  # Convertir la entrada a un número entero
#mejor forma de hacerlo
#heith = int(input("Introduce tu altura en cm: "))  # Convertir la entrada a un número entero
# Verificar si la persona puede montar en la montaña rusa
if heith >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
