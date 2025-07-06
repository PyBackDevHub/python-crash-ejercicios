"""
Script que demuestra como eliminar espacios en blanco y caracteres especiales
(\n\t) de una cadena usando los metodos lstrip(),rstrip(),strip().

se utiliza una cadena que contiene tabulaciones y saltos de linea para ilustrar
el funcionamiento de cada metedo.
"""

#variable con espacios en blanco y caracteres especiales
nombre_persona = "\t\n python developer backend \n\t"

#mostrar el nombre con los espacios y tabulaciones visibles
print("nombre con espacios y tabulaciones:")
print(repr(nombre_persona))

#usar lstrip() para eliminar espacios al inicio
print("\nDespues de lstrip():")
print(repr(nombre_persona.lstrip()))

#usar rstrip() para eliminar espacios al final
print("\nDespues de rstrip():")
print(repr(nombre_persona.rstrip()))

#usar strip() para eliminar espacios al inicio y al final
print("\nDespues de strip()")
print(repr(nombre_persona.strip()))