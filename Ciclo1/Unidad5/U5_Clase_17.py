#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# Tema: Clase 17  Manejo de archivos  (semana7)
# Para: mision tic 2022. 06 Junio 2022 
# # version ='1.0' VsCodium
#TODO:Python Preview Extension

import pandas as pd

data = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}

datosDataFrame = pd.DataFrame(data)

print(datosDataFrame)

#Acaba la implementacion

datosDataFrame.to_csv('example.csv')


fic = open("example.txt", "w", encoding='utf-8') #IMPORTANT: esto es para que funcionen las tildes al importar y exportar

data = ["Linea1", "Linea2", "Linea3", "Linea4", "Línea5"]

for line in data:
    fic.write(line)
    fic.write("\n")
fic.close()
