#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# Tema: reto 2. Script para solucionar el reto 2, version 2
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



def cliente(informacion:dict)-> dict:
    informacion['id_cliente'] = int()
    informacion['nombre'] = str(informacion['nombre'])
    informacion['apto'] = True or False
    if informacion['edad'] >18 :
        informacion['apto'] = True
        informacion['primer_ingreso'] = bool(informacion['primer_ingreso'])
        informacion['atraccion'] = "X-Treme"
        if informacion['primer_ingreso'] != False:
            informacion['total_boleta'] = float(19000)
        else :
             informacion['total_boleta'] = 20000
    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        informacion['apto'] = True
        informacion['primer_ingreso'] = bool(informacion['primer_ingreso'])
        informacion['atraccion'] = "Carros chocones"
        if informacion['primer_ingreso'] != False:
            informacion['total_boleta'] = float(4650)
        else:
             informacion['total_boleta'] = 5000
    elif informacion['edad'] >= 7 and informacion['edad'] < 15:
        informacion['apto'] = True 
        informacion['primer_ingreso'] = bool(informacion['primer_ingreso'])
        informacion['atraccion'] = "Sillas voladoras"
        if informacion['primer_ingreso'] != False:
            informacion['total_boleta'] = float(9500)
        else :
            informacion['total_boleta'] = 10000
    elif informacion['edad'] < 7:
        informacion['apto'] = False
        informacion['atraccion'] = 'N/A'
        informacion['total_boleta'] = 'N/A'
        
    return {'nombre': informacion['nombre'],
            'edad': informacion['edad'],
            'atraccion': informacion['atraccion'],'apto': informacion['apto'],
            'primer_ingreso': informacion['primer_ingreso'],
            'total_boleta': informacion['total_boleta']
            }

c1 ={'id_cliente': 1 , 'nombre' : 'Johana Fernandez', 'edad' : 20, 'primer_ingreso': True}
c2 ={'id_cliente': 1 , 'nombre' : 'Johana Fernandez', 'edad' : 20, 'primer_ingreso': False}
c3 ={'id_cliente': 1 , 'nombre' : 'Gloria Suarez', 'edad' : 3, 'primer_ingreso': True}
c4 ={'id_cliente': 1 , 'nombre' : 'Tatiana Suarez', 'edad' : 17, 'primer_ingreso': True}
c5 ={'id_cliente': 1 , 'nombre' : 'Tatiana Suarez', 'edad' : 17, 'primer_ingreso': False}
c6 ={'id_cliente': 1 , 'nombre' : 'Tatiana Ruiz', 'edad' : 8, 'primer_ingreso': True}
c7 ={'id_cliente': 1 , 'nombre' : 'Tatiana Ruiz', 'edad' : 8, 'primer_ingreso': False}
c8 ={'id_cliente': 1 , 'nombre' : 'Pepito perez', 'edad' : 89, 'primer_ingreso': True}
c8 ={'id_cliente': 1 , 'nombre' : 'Guayaba benitez', 'edad' : 4, 'primer_ingreso': False}

print(cliente(c1))
print(cliente(c2))
print(cliente(c3))
print(cliente(c4))
print(cliente(c5))
print(cliente(c6))
print(cliente(c7))
print(cliente(c8))