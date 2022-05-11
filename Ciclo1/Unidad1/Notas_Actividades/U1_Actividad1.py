#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# En : Ciclo 1 , unidad 1 Actividades, ciclo FOR. mision tic 2022. 9 Mayo 2022 
# # version ='1.0' VsCodium
#Escribir un algoritmo que lea cuatro números e indique cual es el mayor

def mayor(num1:float,num2:float,num3:float,num4:float):
    """La función mayor admite como parametros de entrada 4 números reales, para luego realizar 
    la consulta con la funcion max, con el fin de devolver el número mayor que se usaron como parametros
    de entrada.

    Args:
        num1 (float): _description_
        num2 (float): _description_
        num3 (float): _description_
        num4 (float): _description_

    Returns:
        _Cadena de texto_: Esta cadena le dice al usuario cual es el número mayor
    """
    consultar = (max(num1, num2, num3, num4))
    return f"El número mayor de los 4 es: {consultar}"

print(mayor(2, 98.85, 35.4, 6))