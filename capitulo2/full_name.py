"""
Script que construye y muesta un nombre completo con formato adecuado

Este ejemplo usa un f-string para combinar el primer nombre y el apellido
en una sola cadena
"""

first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(full_name)

message = f"hello, {full_name.title()}!"
print(message)
