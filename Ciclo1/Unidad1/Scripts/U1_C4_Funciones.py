#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# En : Clase 4 ciclo 1 mision tic 2022. 4 Mayo 2022 
# # version ='1.0' VsCodium
# en este caso separamos las funciones en un archivo nuevo

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