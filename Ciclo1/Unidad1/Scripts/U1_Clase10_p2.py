####### Parte 2:
listanumeros = [2,4,6,8,10]

#for posicion in range(0,5): # 0,1,2,3,4 estas son las posiciones, y va a imprimir
#    print(listanumeros[posicion])

#Ahora queremos imprimir el promedio de todos

listanumeros = []
sumatoria = 0 
cantidad_numeros = int(input("Cuantos numeros desea ingresar?: "))
contador_numeros = 0

while contador_numeros < cantidad_numeros:
    numero = float(input("Ingrese un número:  "))
    listanumeros.append(numero)
    contador_numeros += 1 #Siempre incrementamos la var de control
    

for posicion in range(0,len(listanumeros)):
    print(listanumeros[posicion])
    sumatoria += listanumeros[posicion]
    
promedio = sumatoria / len(listanumeros)

print(f"El promedio de los números es : {round(promedio),2}") #FIXME: redondear esta cifra


#Ejemplo 2

lista_nombres = ['Maria', 'Juan', 'Daniel', 'Alejandra', 'Sandra']
lista_aportes = [5000, 10000,22000, 13000, 19000]

#preguntamos al user el nombre que quiere consultar:
nombre = input("Ingrese el nombre de la persona que desee consultar: ")
#primero miramos si esta en la lista, y luego veo la posicion, porque esa posicion es la que consulto en aportes.
#Lo puedo buscar con get?

opcion = int(input(""" Elija una opcion:
    1. Para consultar
    2. Registrar nuevo aporte"""))

if opcion == 1:
    nombre = input("Ingrese nombre de la persona paa quien desee consultar: ")
   
    if nombre in lista_nombres:
        posicion = lista_nombres.index(nombre)
        print(f"{nombre} aportó ${lista_aportes[posicion]}")
    else: #si no entonces
        print(f"{nombre} no ha hecho aportes")
        
elif opcion == 2:
    nombre = input("Ingrese el nombre de la persona que realiza el aporte")
    aporte = float(input("Ingrese el valor del aporte"))
    
    if nombre in lista_aportes:
        posicion = lista_aportes.index(nombre)
        lista_aportes[posicion] = lista_aportes[posicion] + aporte
    else:
        lista_nombres.append(nombre)
        lista_aportes.append(aporte)