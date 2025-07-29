prompt = "deli ya no tiene especialidad pastrami"

sandwich_orders = [
    "BLT",
    "Club Sándwich",
    "Croque Monsieur",
    "pastrami",
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
    "pastrami",
    "Butifarra",
    "Barros Luco",
    "Chacarero",
    "Sándwich de aguacate y hummus",
    "Sándwich de vegetales asados",
    "Sándwich de tofu y espinacas",
    "Sándwich de lentejas",
    "Sándwich de queso vegano y palta",
    "pastrami",
    "Sándwich de atún",
    "Sándwich de pollo a la parrilla",
    "Sándwich de jamón y queso",
    "Sándwich de mantequilla de maní y mermelada"
]

print(prompt)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("lista final sin pastrami")
print(sandwich_orders)
