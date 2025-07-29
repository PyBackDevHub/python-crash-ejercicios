sandwich_orders = [
    "BLT",
    "Club Sándwich",
    "Croque Monsieur",
    "Philly Cheesesteak",
    "Reuben",
    "Panini",
    "Tramezzino",
    "Shawarma",
    "Döner Kebab",
    "Bánh mì",
    "Pambazo",
    "Cemita",
    "Guajolota",
    "Choripán",
    "Chivito",
    "Butifarra",
    "Barros Luco",
    "Chacarero",
    "Sándwich de aguacate y hummus",
    "Sándwich de vegetales asados",
    "Sándwich de tofu y espinacas",
    "Sándwich de lentejas",
    "Sándwich de queso vegano y palta",
    "Sándwich de huevo duro",
    "Sándwich de atún",
    "Sándwich de pollo a la parrilla",
    "Sándwich de jamón y queso",
    "Sándwich de mantequilla de maní y mermelada"
]

#lista vacia
finished_sandwiches = []
#verificar ususarios hasta que no alla 
#condicion
while sandwich_orders:
    #eliminar elementos de la primera lista
    actual_sandwich = sandwich_orders.pop()#con parametros para que sea mostrado como pidieron
    #mostrar el estado actual de transicion
    print(f"verifcar sandwich:{actual_sandwich.title()}")
    #agregar a lista nueva
    finished_sandwiches.append(actual_sandwich)
#mostrar usuarios confirmados
print("\n--- resultados lista ---")

for finished_sandwich in finished_sandwiches:
    print(f"lista de nueva: {finished_sandwich.title()}")