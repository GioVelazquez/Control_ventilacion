# - SISTEMA DE MEDICION DE VENTANA DESLIZABLE -
# POR: GIOVANNI VELAZQUEZ AVILEZ
# ESTUDIANTE DEL ITZ DE ING ELECTROMECANICA
# RESIDENTE EN EL IER-UNAM, AGO-DIC 2020

#Se importan los modulos y funciones 
import machine
from machine import Pin
import time
from time import sleep
import math
from funcion import *
from funciones import *
from wifi import activate_wifi
import utime

#Se establecen los datos de conexion a la red 
red = 'TOTALPLAY_897E2E'
clave = 'EZ04022ST1'

#Se establecen los datos de conexion a ThingsBoard
unique_id = '70099f70-10a1-11eb-9c3f-d1ead9980bc3'
token = 'MdihxoaKm0rTUqo9GiRm'


label ='distancia' #Nombre de la etiqueta con la que se publicaran los datos 

activate_wifi(red,clave)

#Led parpadea cuando el ESP8266 sale del deepsleep
led = Pin (2, Pin.OUT)
led.value(0)
sleep(1)
led.value(1)
sleep(1)

while True:

	print ('DISTANCIA')
	for count in range(2): #Se hace uso de un ciclo for count para devolver 2 mediciones
		result=distancia_media() 
		print (result, 'cm')
		valor = result
		data  = {label: valor} #Se asignan los valores para el data
		publish_thingsboard(red,clave,token, unique_id,data) #se publican los datos en ThingsBoard
		sleep(1)
	
	
	print('IRE A DORMIR')
	sleep(3)
	
	machine.deepsleep() #El ESP8266 entra en modo "sueño profundo"

        
