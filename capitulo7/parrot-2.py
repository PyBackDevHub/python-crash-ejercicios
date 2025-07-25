prompt = input("Tell me something, and I will repeat it back to you: ")
prompt += "\nEnter 'quit' to end the program."# agregar mensaje de salida

message = ""#incializar variable
while message != 'quit':#verificar si el mensaje es diferente de 'quit'
    message = input(prompt)# solicitar entrada del usuario
    if message != 'quit':#verificar si el mensaje es diferente de 'quit'
        print(f"muestra la palabra: {message}")# mostrar el mensaje ingresado
print("================")
"""
Resumen de diferencias
Primer bloque: El mensaje de instrucciones depende de lo que el usuario escribió al principio,
lo que puede ser confuso.

Segundo bloque: El mensaje de instrucciones es fijo y claro en cada iteración, 
lo que mejora la experiencia del usuario y la claridad del código.
"""
active = True#inicializar variable, para controlar el bucle llamada flag
while active:#mientras la variable sea verdadera
    message = input(prompt)#solicitar entrada del usuario

    if message == 'quit':#verificar si el mensaje es igual a 'quit'
        active = False# cambiar la variable a falsa
    else:
        print(f"muestra la palabra: {message}")
print("Gracias por participar")#mensaje de despedida