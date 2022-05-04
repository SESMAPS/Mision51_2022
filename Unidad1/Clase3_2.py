#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
#----------------------------------------------------------------------------
# Created By  : Cristian ospina
# Created: Clase 3 ciclo 1 mision tic 2022. Parte 2 , Continua en clase3_2.py
# version ='1.0' El ejercicio de ayer de lenguaje natural a código. Se ingresan 2 números y evalua e imprime cual es el mayor

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print(f"El número mayor es: {num1}") #Ojo con la identación. Debe estar dentro del condicional 1tabulacion. Si no es así se ejecutaria siempre
else:
    if num2 > num1:
      print("El número mayor es: {num2")
    else:
        print("Los dos números son iguales") #Sin necesidad de evaluar la igualdad ==


print("Fin del programa")