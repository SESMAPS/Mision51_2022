#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#programa que encuentra el mayor de 4 números ingresados por el usuario
Created on Tue May  3 13:08:59 2022

@author: davoc
"""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercero número: "))
num4 = int(input("Ingrese el cuarto número: "))

#Condiciones anidadas
#Si bien el algo funciona, deberia detenerse cuando encuentre el numero mayor, en lugar de seguir evuluandolo.
if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"El número mayor es: {num1}")
if num2 > num1 and num2 > num3 and num2 > num4:
    print(f"El número mayor es: {num2}")
if num3 > num1 and num3 > num2 and num3 > num4:
    print(f"El número mayor es: {num3}")
if num4 > num1 and num4 > num2 and num4 > num3:
    print(f"El número mayor es: {num4}")
    

# Entonces lo podemos reescribir así:
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    print(f"El número mayor es: {num1}")
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
        print(f"El número mayor es: {num2}")
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    print(f"El número mayor es: {num3}")
elif num4 >= num1 and num4 >= num2 and num4 >= num3:
    print(f"El número mayor es: {num4}")
elif num1 == num2 == num3 ==num4:
    print("los números son iguales")
print ("ya encontré el numero mayor")

# Entonces lo podemos reescribir así:

if num1 == num2 == num3 ==num4:
    print("los numeros son iguales")
elif num1 >= num2 and num1 >= num3 and num1 >= num4:
    print(f"El número mayor es: {num1}")
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
        print(f"El número mayor es: {num2}")
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    print(f"El número mayor es: {num3}")
elif num4 >= num1 and num4 >= num2 and num4 >= num3:
    print(f"El número mayor es: {num4}")

print ("ya encontré el numero mayor")