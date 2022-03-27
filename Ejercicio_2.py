"""Ejercicio_2: Realiza un programa que lea un número impar por teclado. 
Si el usuario no introduce un número impar, debe repetise el proceso
 hasta que lo introduzca correctamente."""
while True:#Inicio de la funcion while
    n1=int(input("Por favor ingrese un número impar: "))#Se pide al usuario que ingrese un número
    if n1%2==0:#Si el módulo del número es igual a 0, es par
        print("El número que introdujo es par.")
    else:#Si el módulo del número es impar, se rompe el ciclo.
        print("Fin del ciclo")
        break


