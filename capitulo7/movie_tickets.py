
while True:
    edad = int(input("ingrese su edad para saber el precio su boleto"))
    if edad == 0:
        break
    if edad < 3:
        print("usted entra gratis")
    elif 3 <= edad <=12 :
        print("usted paga $10")
    else:
        print("usted paga $15")