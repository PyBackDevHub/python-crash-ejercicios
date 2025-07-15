# Pruebas condicionales en Python

# ---------------------------
# Igualdad y desigualdad con cadenas
# ---------------------------
nombre = 'Ana'
print("¿El nombre es 'Ana'? Predigo True.")
print(nombre == 'Ana')  # True

print("\n¿El nombre es 'Carlos'? Predigo False.")
print(nombre == 'Carlos')  # False

# ---------------------------
# Uso del método lower()
# ---------------------------
ciudad = 'Bogotá'
print("\n¿La ciudad en minúsculas es 'bogotá'? Predigo True.")
print(ciudad.lower() == 'bogotá')  # True

print("\n¿La ciudad en minúsculas es 'Bogotá'? Predigo False.")
print(ciudad.lower() == 'Bogotá')  # False

# ---------------------------
# Pruebas numéricas
# ---------------------------
edad = 25

print("\n¿La edad es igual a 25? Predigo True.")
print(edad == 25)  # True

print("\n¿La edad es diferente de 30? Predigo True.")
print(edad != 30)  # True

print("\n¿La edad es mayor que 18? Predigo True.")
print(edad > 18)  # True

print("\n¿La edad es menor que 18? Predigo False.")
print(edad < 18)  # False

print("\n¿La edad es mayor o igual a 25? Predigo True.")
print(edad >= 25)  # True

print("\n¿La edad es menor o igual a 20? Predigo False.")
print(edad <= 20)  # False

# ---------------------------
# Uso de 'and' y 'or'
# ---------------------------
altura = 170
peso = 65

print("\n¿La edad es mayor que 20 y el peso menor que 70? Predigo True.")
print(edad > 20 and peso < 70)  # True

print("\n¿La edad es menor que 20 o el peso mayor que 70? Predigo False.")
print(edad < 20 or peso > 70)  # False

# ---------------------------
# Verificar si un elemento está en una lista
# ---------------------------
frutas = ['manzana', 'banana', 'pera']

print("\n¿'banana' está en la lista de frutas? Predigo True.")
print('banana' in frutas)  # True

print("\n¿'sandía' está en la lista de frutas? Predigo False.")
print('sandía' in frutas)  # False

# ---------------------------
# Verificar si un elemento NO está en una lista
# ---------------------------
print("\n¿'mango' no está en la lista de frutas? Predigo True.")
print('mango' not in frutas)  # True

print("\n¿'pera' no está en la lista de frutas? Predigo False.")
print('pera' not in frutas)  # False
