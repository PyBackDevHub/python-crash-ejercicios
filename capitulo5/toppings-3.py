requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

print("==============")
#ejercicio con lista vacia
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza!")
    else:
        print("Are you sure you want a plain pizza?")
#comparacion de dos lista
print("=============")
#elementos disponibles de pizza
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
#elementos pedidos por el cliente
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
#se checa cada elemento en elementos disponibles con la de elementos pedidos por el cliente
for requested_topping in requested_toppings:
    if requested_topping in requested_toppings:
        print(f"Adding{requested_topping}")
    else:
        print(f"sorry, we dont have{requested_topping}")
print("\nFinish making your pizza")
