#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# Tema: reto 2. Script para solucionar el reto 2
# Para: mision tic 2022. 17 Mayo 2022 
# # version ='1.0' VsCodium

# En el parque de diversiones “AVENTURAS EXTREMAS” se requiere implementar una función en la
# cual reciba como parámetro un diccionario.
# Esta función debe retornar un nuevo diccionario con las llaves nombre, edad, atracción,
# primer_ingreso, total_boleta y apto del cliente:
# • En donde apto tendrá como valor una variable booleana, será verdadera si su edad cumple con
# los rangos exigidos en la tabla anterior, en el caso contrario será falsa.
# • En el caso de atraccion y total_boleta, si no se cumple el rango de edades se le asignara un valor
# de ‘N/A’ a cada uno.
# • Si primer_ingreso es verdadero, el total_boleta será el valor de la boleta menos el descuento de
# lo contrario se pagará el valor neto de la boleta

#No sirve este código.


def cliente(info:dict)-> dict:
    info['id_cliente'] = int(input()) #De esta forma puedo asegurarme que el dato de entrada cumpla sea de ese tipo?
    info['nombre'] = str(input())
    info['edad'] = int(input()) 
    info['primer_ingreso'] = bool(input())
    #Atraccion X-Treme
    if info['edad'] > 18 and info['primer_ingreso'] == True:
        info['atraccion'] = "X-Treme"
        info['total_boleta'] = 20000 * 0.05
        es_apto['Es apto'] = "apto"
    else:
        info['atraccion'] = "X-Treme"
        info['total_boleta'] = 20000 
    #Atraccion Carros chocones
    if info['edad'] >=18 and info['edad'] <=18 and info['primer_ingreso'] == True:
        info['atraccion'] = "Carros chocones"
        info['total_boleta'] = 5000 * 0.07
    else:
        info['atraccion'] = "Carros chocones"
        info['total_boleta'] = 7000
    #Atraccion Sillas voladoras
    if info['edad'] >18 and info['primer_ingreso'] == True: 
        info['atraccion'] = "Sillas voladoras"
        info['total_boleta'] = 10000 * 0.05
    else:
        info['atraccion'] = "Sillas voladoras"
        info['total_boleta'] = 10000 
    
    return {{nombre}: info['nombre'],
            {edad}: info['edad'],
            {atraccion}: info['atraccion'],
            {primer_ingreso}: info['primer_ingreso'],
            {total_boleta}: info['total_boleta']
            }

prueba ={'id_cliente': 1 , 'nombre' : 'Johana Fernandez', 'edad' : 20, 'primer_ingreso': True}
print (type(prueba))
print (cliente(prueba))

