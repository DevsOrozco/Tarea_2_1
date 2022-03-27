"""Ejercicio 5 
Realiza un programa que pida al usuario un número entero del 0 al 9, 
y que mientras el número no sea correcto se repita el proceso. 
Luego debe comprobar si el número se encuentra en la lista de números y notificarlo: """

lista=[0,1,2,3,4,5,6,7,8,9]#Se crea una lista con números enteros del 0 al 9

n1=int(input("Por favor ingrese un número del 0 al 9: "))#Se pide al usuario que ingrese un número entero
while True:#Se inicia el ciclo
    if n1 not in lista:#Si el número no se encuentra en la lista, se indica al usuario este mensaje y se pide que ingrese un número del 0 al 9
        print("El número que ingreso no se encuentra en el rango 0 a 9")
        n1=int(input("Por favor ingrese un número del 0 al 9: "))#Se almacena el valor ingresado y se continúa con el ciclo
    else:
        print("El numero que ingresó está en al base de datos")#Si el número está en la lista, se le indica al usuario este mensaje y se termina el ciclo
        break


