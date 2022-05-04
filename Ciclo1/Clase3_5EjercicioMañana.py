#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
#----------------------------------------------------------------------------
# Created By  : davoc
# Created: Clase 3 ciclo 1 mision tic 2022. Parte 5 , Tarea
# version ='1.0'

#Se trata de escribir el algoritmo que permita calcular el valor a pagar para una compra de un articulo determinado 
#del que se adquieren una o varias unidades. El iva a aplicar es del 19% y si el precio bruto(precio de venta mas IVA)
#es mayor de 500.000 COP, se aplicará un descuento del 6.5% sobre el total.
#Se debe pedir al usuario que ingrese el valor del articulo y la cantidad.
import sys

numero_producto = int(input("Cuantos productos compró?: ")) #solo admite enteros de la cantidad total de articulos.
precio_articulo = float(input("Cuanto costó un producto?: ")) #funciona con float usando . pero no con comas

total_sin_iva = precio_articulo * numero_producto
precio_bruto = precio_articulo * numero_producto * 0.19 + precio_articulo * numero_producto
#el precio bruto antes del + solo calcularia el iva de esos producto, entonces le sumo de nuevo las var
#podria almacenar el total del iva en una var nueva, y en la sumarla a precio sin iva


print(f"El precio total sin iva es de : {total_sin_iva}")
print(f"El precio total con iva es de : {precio_bruto}")