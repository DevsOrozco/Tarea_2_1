"""Ejercicio 7
 Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, 
 pero no debe repetise ningún elemento en la nueva lista:"""

lista1=[]#Se crea un alista vacía
size1=int(input("Por favor ingrese el número de valores de la primera lista: "))#Se solicita al usuario el tamaño de la lista
print("Por favor ingrese los valores a la lista 1: ")#Se solicita al usuario que ingrese los valores de la lista
for i in range (0,size1):#Se ingresan los valores de la lista según su tamaño
    n1=input()
    lista1.append(n1)
    i+=1
lista2=[]#Se crea un alista vacía
size2=int(input("Por favor ingrese el número de valores de la primera lista: "))#Se solicita al usuario el tamaño de la lista
print("Por favor ingrese los valores a la lista 2: ")#Se solicita al usuario que ingrese los valores de la lista
for i in range (0,size2):#Se ingresan los valores de la lista según su tamaño
    n2=input()
    lista2.append(n2)
    i+=1

print ("Lista 1: ",lista1)# Se imprimen los valores de las listas
print ("Lista 2: ",lista2)

lista3=[]#Se crea la tercera lista, donde se recopilarán los valores repetidos de ambas listas
for i in lista1:#Se comparan los elementos de las dos listas
    for j in  lista2:
        if(i==j and i not in lista3):#Si el elemento en la lista 1 es distinto al elemento de la lista 2, y no se encuentra repetido en la lista 3
            print(i)
            lista3.append(i)#Se añade el número a la lista 3
print("Lista numeros repetidos: ",lista3)#Se imprime la lista de números repetidos

