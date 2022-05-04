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

def area_triangulo(base,altura):
    area = base * altura / 2
    return area

#Vamos a preguntar al usuario base y altura, para que calcule el área
baset = float(input("Ingrese la base del triangulo: "))
alturat = float(input("Ingrese la altura del triangulo: "))
area = area_triangulo(baset, alturat)
print(f"El área del triangulo es: {area}")