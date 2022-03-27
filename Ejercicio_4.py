"""Ejercicio 4 Realiza un programa que pida al usuario cuantos números 
quiere introducir. Luego lee todos los números y realiza una media aritmética:"""

n1=int(input("Ingrese el número de valores que quiere introducir: "))#Le pido al usuario que indique el número de valores que desea ingresar
suma=0#Declaro la variable suma
print("Ingrese los valores que desea introducir: ")
for i in range(0,n1):#Inicio la funcion for para i en el rango 0 a el número de valores que desea ingresar el usuario
    n2=int(input())
    suma+=n2#Sumo el valor que ingresó el usuario a la suma
    i+=1#Sumo 1 al contador
print("La media es: ",suma/n1)#Imprimo la media (suma de valores/número de valores ingresados)