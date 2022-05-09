#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por  : davoc
# En : Reto 1 ciclo, modificado luego de presentar la prueba. Resultado 4 sobre 5. 1 mision tic 2022. 7 Mayo 2022 
# # version ='12.0' VsCodium
"""Una entidad Bancaria o entidad financiera, requiere calcular
el valor de los intereses ganados y el total final de dinero para diferentes clientes, de
acuerdo, a una cantidad de dinero invertida en un CDT. Un CDT por su parte, es un
producto financiero que ofrece la posibilidad de guardar dinero durante un tiempo
determinado para recibir posteriormente sus intereses devengados, asimismo, ofrece
rendimientos a una tasa fija, asegurando una rentabilidad libre de riesgo en un tiempo
determinado que por lo general debe ser mayor a dos (2) meses. Si, este dinero se retira
antes de este periodo se aplica una penalidad del 2%.
En ese sentido, el valor de los intereses ganados por un periodo de tiempo superior a dos
meses se determina a través de la siguiente formula:

Para responder a este planteamiento, escriba una función que reciba como parámetros:
una cadena con el usuario del cliente como dato alfanumérico, el capital aportado y el
tiempo del CDT y, en consecuencia, retorne una cadena de caracteres que le proporcione
al banco la información que desea obtener.
La cadena debe tener para el caso de las ganancias, la siguiente estructura:
“Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un
tiempo de {} meses es: {}”
para el caso de las pérdidas:
“Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un
tiempo de {} meses es: {}”

    """
# Creacion de la funcion
def CDT(usuario:str,capital:int,tiempo:int):#

    if tiempo > 2:
        porcentaje_interes = 0.03
        valortotal = capital+capital * porcentaje_interes * tiempo /12
        mensaje = print((f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valortotal}"))
        return  mensaje 
        #return = (f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valortotal}"))


    if tiempo <= 2: # si se abre un if es obligatorio el else? o elif? en este caso como no es un ciclo no es necesario detenerlo?
        porcentaje_aperder = 0.02
        valoraperder = capital * porcentaje_aperder
        valortotalp = capital - valoraperder
        return (f"Para el usuario {usuario} ({type(usuario)}) La cantidad de dinero a recibir, según el monto inicial {capital}({type(capital)}) para un tiempo de {tiempo} ({type(tiempo)}) meses es: {valortotalp}({type(valortotalp)})")

print(CDT("AB1012", 1000000, 3))
print(CDT("ER3366", 65000, 2))
usuario = "carlos"
print(type(usuario))

#Si quiero tomar los datos de entrada del usuario
usuario = str(input("Cual es su nombre de usuario: "))
capital = int(input("Monto a invertit: ")) #si el usuario entra un float, como hago para transformarlo a entero?
tiempo = int(input("Tiempo en meses: ")) #este tiempo es en meses
calculado = CDT(usuario, capital, tiempo) # el valor final lo quiero formatear con 3 decimales cuando tenga decimales, de lo contrario que quede como entero
print(f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {calculado}")


#TODO quiero que muestre un mensaje en pantalla pidiendo al usuario introducir los valores de las 3var. E imprimir el resultado.abs(x)
# y si quiero consultar el tipo de cada variable que se usó dentro de una funcion como se hace?