#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
#----------------------------------------------------------------------------
# Created By  : Cristian ospina
# Created: Clase 3 ciclo 1 mision tic 2022. Parte 1 , Continua en clase3_2.py
# version ='1.0'

num1 = 8
num2 = 9
suma = num1 + num2

print(f"El valor de la suma es: {suma}") #la f significa que voy a formatear el mensaje que va a imprimir. 
#Si es + es para concatenar,  y deberia entonces convertir en un str e valor de la suma- Porque concatenar solo es para texto
#por eso se convierten los num a cadena de txt
#print(f"El valor de la suma es:" + str {suma})
print(f"El valor de la suma es: {suma}, el primer número es {num1} y el segundo es {num2}")

nombre = "Pepito"
apellido = "Perez"
edad = 23

nombre_completo = nombre +" " + apellido + "(" +str(edad) +"años)"
print(nombre_completo)

tunombe = input("Como te llamas: ")
num3 = int(input("Ingrese el primer número: ")) #con este input solo está entrando como cadenas de texto, por eso la suma concatena
num4 = int(input("Ingrese el segundo número: "))
sumaentrada = num3 + num4
print(f"El valor de la suma es: {sumaentrada}")

print(type(suma))# devuelve que tipo de dato se está almacenado. Pero si quiero que me devuelva de dos variables o mas?
