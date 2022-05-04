#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# En : Clase 4 ciclo 1 mision tic 2022. 4 Mayo 2022 
# # version ='1.0' VsCodium
#
#Escribir un algoritmo que permita calcular cualquiera de las siguientes opciones:
#• La superficie de un triángulo.
#• El área de un círculo.
#• La base de un triángulo, teniendo la superficie y la altura.
#• El radio de un círculo, teniendo el área.
import math

def area_triangulo(base,altura): #las funciones siempre van al comienzo, no al final del code
    area = base * altura / 2
    return area
def area_triangulo2(base:float,altura:float): #de esta restringimos a que sean numeros flotantes
    area = base * altura / 2
    return area

def area_circulo(radio:float):
    area = 3.1416 * radio ** 2
    return area

def base_triangulo(area:float,altura:float):
    base = 2* area / altura
    return base

def radio_circulo(area:float):
    radio = math.sqrt(area / math.pi)
    return radio



#area = area_triangulo(baset, alturat)
#print(f"El área del triangulo es: {area}")

#print(f"El area del triangulo es : {area_triangulo(baset, alturat)}") # de esta forma se imprime calculandolo directamente

opcion = int(input("""Elija una opción:
1. Area de un triangulo=
2. Area de un circulo=
3. Base de un triangulo=
4. Radio de un circulo="""))

if opcion == 1: #El user decidio calcular area triangulo
    #Vamos a preguntar al usuario base y altura, para que calcule el área
    baset = float(input("Ingrese la base del triangulo: "))
    alturat = float(input("Ingrese la altura del triangulo: "))
    area = area_triangulo2(baset, alturat)
    print(f"El area del triangulo es: {area}")
elif opcion == 2:
    radioc =float(input("Ingrese el radio del circulo: "))
    area = area_circulo(radioc)
    print(f"El area del circulo es: {area}")
elif opcion == 3:
    areat =float(input("Ingrese la base del triangulo: "))
    alturat = float(input("Ingrese la altura del triangulo: "))
    baset = base_triangulo(areat, alturat)
    print(f"La base del triangulo es: {baset}")
elif opcion == 4:
    areac = float(input("Ingrese el area del circulo: "))
    radio = radio_circulo(areac)
    print(f"El radio del circulo es: {radio}")