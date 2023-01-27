'''
Ejercicio 1
Se tiene un sistema embebido con un sensor de temperatura y otro de humedad. Existe un servicio
que lee dichos sensores accediendo al hardware y deja los valores en un archivo llamado
“sensores.data” el cual tiene el siguiente formato:
XX.X,XX.X
Donde el primer valor es el de temperatura, luego mediante una coma se separa el otro valor que es
la humedad.
Realizar un servicio web que devuelva en formato JSON la información de estos sensores de
temperatura y humedad. Este servicio será consumido por una página web y una app móvil donde
se puedan visualizar los datos:
El servicio web tendrá la dirección cgi-bin/sensors.py y deberá devolver la información con el
formato:

{"temp":"30.4","hum":"47.3"}

Se deberá leer la información desde el archivo, generar el JSON y devolverlo. Para probar el
servicio, abrir un navegador en localhost:8080/cgi-bin/sensors.py. Se deberá observar el texto en
formato JSON.
'''
import json
from random import *

def valor_sensores():
    cantidad_valores = randint(1,4)
    try:
        archivo = open('sensoresData.txt', 'wt')
        for i in range(cantidad_valores):
            temp = str(round((random() * 45),2))
            hum = str(round((random()* 100), 2))
            archivo.write(temp + ',' + hum + '\n')
        print('archivo creado exitosamente')
    except OSError:
        print('No se pudo grabar el archivo')
    finally:
        try:
            archivo.close()
        except NameError:
            pass

def json_creator():
    try:
        archivo = open('sensoresData.txt', 'rt')
        linea = archivo.readline()
        lista = []
        while linea:
            temp, hum = linea.split(',')
            hum = hum.rstrip('\n')
            data = {
                'temp': temp,
                'hum': hum
            }
            lista.append(data)
            linea = archivo.readline()
        sensoresJSON = json.dumps(lista)
        print('archivo leido exitosamente')
        
        return sensoresJSON
    except FileNotFoundError:
        print('No se pudo encontrar el archivo: ')
    except OSError:
        print('No se puede leer el archivo: ')
    finally:
        try:
            archivo.close()
        except NameError:
            pass


valor_sensores()
json_creator()



