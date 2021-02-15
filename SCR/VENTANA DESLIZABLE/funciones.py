import machine
import time
from machine import Pin
import utime

def distancia_normal():
	#se asigna el Pin TRIG	- emisor
	trig=machine.Pin(14, machine.Pin.OUT)
	trig.off() #el Pin esta apagado
	utime.sleep_us(2)
	trig.on() #el Pin esta encendido
	utime.sleep_us(10)
	trig.off()
	#se asigna el Pin ECHO - receptor
	echo=machine.Pin(12, machine.Pin.IN)
	while echo.value() == 0: #Mientras es valor del Pin echo sea 0
		pass
	t1 = utime.ticks_us()    #T1 sera igual al tiempo transcurrido mientras esta esa condicion
	while echo.value() == 1: #Cuando el valor del Pin echo sea 1
		pass
	t2 = utime.ticks_us()    #T2 sera igual al tiempo transcurrido hasta esa condicion
	cm = ((t2 - t1)*0.03432)/2 #Se aplica la formula para obtner la distancia en cm (cm=((t2-t1)*velocidadelsonido)/2)
	utime.sleep_ms(20) #tiempo recomendado entre una y otra medicion
	return cm #devuelve la distancia en cm
	
				
def distancia_media():
	# inicia la lista
    	distancia_muestras = [] 
    	# toma 10 muestras y las agrega a la lista
    	for count in range(10):
        	distancia_muestras.append((distancia_normal()))
        	utime.sleep_ms(20)
    	# abre la lista
    	distancia_muestras = sorted(distancia_muestras)
    	# toma el valor medio de la lista de valores 
    	distancia_media = distancia_muestras[int(len(distancia_muestras)/2)]
    	

    	#print(distancia_muestras) #imprime los valores de la lista (imprimir es opcional)
	return float(distancia_media)
	

