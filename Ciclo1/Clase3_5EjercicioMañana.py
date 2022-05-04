#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
#----------------------------------------------------------------------------
# Created By  : davoc
# Created: Clase 3 ciclo 1 mision tic 2022. Parte 5 , Tarea para el 4 Mayo 2022
# version ='2.0'

#Se trata de escribir el algoritmo que permita calcular el valor a pagar para una compra de un articulo determinado 
#del que se adquieren una o varias unidades. El iva a aplicar es del 19% y si el precio bruto(precio de venta mas IVA)
#es mayor de 500.000 COP, se aplicará un descuento del 6.5% sobre el total.
#Se debe pedir al usuario que ingrese el valor del articulo y la cantidad.

numero_producto = int(input("Cuantos productos compró?: ")) #solo admite enteros de la cantidad total de articulos. #!!restringir a enteros positivos
precio_articulo = float(input("Cuanto costó el producto?: ")) #funciona con float usando . pero no con comas
#Como puedo hacer para que reconozca el formato del usuario, ya que en unos paises
#el punto es usado como separador decimal, mientras que la coma como separador de miles, y viceversa?

total_sin_iva = precio_articulo * numero_producto
precio_bruto = precio_articulo * numero_producto * 0.19 + precio_articulo * numero_producto
diferencia_promo = 500000 - total_sin_iva

#el precio bruto antes del + solo calcularia el iva de esos producto, entonces le sumo de nuevo las var
#podria almacenar el total del iva en una var nueva, y en la sumarla a precio sin iva
if precio_bruto >= 500000:
    precio_promo = precio_articulo * numero_producto * 0.065 + precio_articulo * numero_producto
    ahorro_compra = precio_bruto - precio_promo
    print(f"El total a pagar con la promo es de: {precio_promo} , y su ahorro en esta compra es de {ahorro_compra}")
else:
    print(f"Lo sentimos, te faltó : {diferencia_promo} para aplicar la promo")
    #print(f"Lo sentimos, te faltó {total_sin_iva}-{tope_promo} para aplicar la promo}")    Se pueden hacer operaciones de resta en un print?  

print(f"El precio total sin iva es de : {total_sin_iva}")
print(f"El total a pagar con iva del 19% sin la promo es de : {precio_bruto}")
""" FIXME: Solucionar:funciona
pero al introducir 1 articulo con precio de 499mil, le aplica el descuento
"""