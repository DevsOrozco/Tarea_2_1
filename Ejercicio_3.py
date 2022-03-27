"""Ejercicio 3 
Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:
Sugerencia: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. 
tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo."""

sum=0#Declaro la variable suma
for i in range(0,101,2):#Uso la función for para sumar los valores del rango mayor a 0 y menor a 101.
    sum+=i
print(sum)#Se imprime la suma