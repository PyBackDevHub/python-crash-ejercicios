#guardar informacion sobre la pizza siendo ordenada
pizza = {
    'crust': 'thick',
    'toppings' : ['mushrooms','extra cheese'],
}

#resume de orden de pizza
print(f"usted ordena una {pizza['crust']}-crust pizza"
      "con los siguientes ingredientes:")
#iteracion de lista de toppings
print("muesta elementos dentro de la lista:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
