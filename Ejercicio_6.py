"""Ejercicio 6 
Utilizando la función range() y la conversión a listas genera las 
siguientes listas dinámicamente:
Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
"""
print("*Listas*")
lista1= list(range(0,11))#Lista de números del 0 al 10
lista2=list(range(-10,1))#Lista de números del -10 al 0
lista3=list(range(0,21,2))#Lista de números pares del 1 al 20 
lista4=list(range(-19,0,2))#Lista de números impares del -20 al 0 
lista5=list(range(0,51,5))

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)