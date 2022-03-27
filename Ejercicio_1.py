""" 
Ejercicio1: Realiza un programa que lea dos números por teclado 
y permita elegir entre 3 opciones en un menú:
Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de no introducir una opción inválida, el programa informará de que no es correcta."""

print("*Operaciones numéricas*\n")
print("Por favor, escriba un número:")#Se pide al usuario que ingrese un número y se almacena
n1=int(input())
print("Por favor, escriba otro número")#Se pide al usuario que ingrese otro número y se almacena
n2=int(input())
while True:
    print("¿Qué operación desea realizar? Elija un numero del 1 al 6\n")#Se muestra el Menú
    print("1:Suma")
    print("2:Resta")
    print("3:Multiplicacion")
    print("4:División")
    print("5:Salir")
    
    n3=int(input())#Se almacena el valor en la variable n3
    suma=n1+n2
    if n3==1:#Suma
        print("Suma de",n1,"y",n2,":",suma)
        break
    if n3==2:#Resta
        print("Resta de",n1,"y",n2,":",n1-n2)
        break
    if n3==3:#Multiplicacion
        print("Multiplicación de",n1,"y",n2,":",n1*n2)
        break
    if n3==4:#Division
        print("División de",n1,"y",n2,":",n1/n2)
        break
    if n3<1 or n3>5:#Error
        print("El numero que ingresón no está en el menú")#Se muestra el mensaje de error y se repite el ciclo
    else:
        print("Hasta la próxima\n*Fin de las operaciones*")#Se muestra un mensaje de despedida
        break
    


 