# - SISTEMA DE CONTROL DE VENTILAS -

# POR: GIOVANNI VELAZQUEZ AVILEZ
# ESTUDIANTE DEL ITZ DE ING ELECTROMECANICA
# RESIDENTE EN EL IER-UNAM, AGO-DIC 2020

import machine
import gc
import network, utime, ntptime, time
from wifi import activate_wifi
from funcion import *
from funciones import *
import funcionesMPU
from funcionesMPU import *
from machine import I2C, Pin, DAC
from esp32_i2c_lcd import I2cLcd 
import math
gc.enable()

red = 'TOTALPLAY_897E2E'
clave = 'EZ04022ST1'
unique_id = '70099f70-10a1-11eb-9c3f-d1ead9980bc3'
token = 'MdihxoaKm0rTUqo9GiRm'
activate_wifi(red,clave)

label ='modulacion'
label2='inclinacion'

lcd = I2cLcd(I2C(scl=Pin(26), sda=Pin(13)), 0x27, 4, 20)
dac1=DAC(Pin(25))
buton1 = Pin(15, Pin.IN) 
buton2 = Pin(4, Pin.IN) 
buton3 = Pin(17, Pin.IN) 
buton4 = Pin(18, Pin.IN)

# LIMPIAR LCD
def lcd_clear():
    lcd.move_to(0, 0)
    lcd.putstr(" " * 80)

# MOSTRAR TEXTO EN LCD
def lcd_show(text, line):
    lcd.move_to(0, line)
    lcd.putstr(text)
    
web_query_delay = 600000
timezone_hour = 6 #ZONA HORARIA

local_time_sec = utime.time() + timezone_hour * 3600
local_time = utime.localtime(local_time_sec)
update_time = utime.ticks_ms() - web_query_delay

lcd_show("B I E N V E N I D O",0)
lcd_show("SISTEMA DE CONTROL",1)
lcd_show("   DE VENTILAS",2)
sleep(3)
lcd_clear()
	

while True:
	
	led.value(0)
	if __name__ == "__main__":
		i2c = I2C(scl=Pin(12), sda=Pin(14))
		mpu6050_init(i2c)
		grados=mpu6050_get_accel_angle_zx(i2c)
   
	while True:
		
		if (grados > 0) and (grados <= 23):
			
			print ('-------> NIVEL DE APERTURA <-------')
			lcd_show("ABIERTAS: 25%",0)
			lcd_show("  CAMBIAR EL",1)
			lcd_show("NIVEL DE APERTURA?",2)
			lcd_show("SI        NO",3)
		
			if  buton4.value() is 0:
				horario_programado()
				lcd_clear()
				lcd_show("ELIJA EL NIVEL DE",0)
				lcd_show("APERTURA DESEADO",1)
				sleep(3)
				lcd_clear()
				lcd_show("USE EL BOTON ARRIBA",0)
				lcd_show("  Y ABAJO PARA",1)
				lcd_show("  DESPLAZARSE",2)
				sleep(3)
				lcd_clear()
				result2=todo25()
				
				i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				
				valor = result2
				valor2 = grados
				data  = [{label: valor}, 
				{label2: valor2}]
				publish_thingsboard(red,clave,token, unique_id,data)
				sleep(3)
				horario_programado()
				
			elif buton2.value() is 0:
				lcd_clear()
				sleep(2)
				
				horario_programado()
				break
			else:
				continue	
			break
			
    		elif (grados > 23) and (grados <= 45):	
    			horario_programado()	
			lcd_show("ABIERTAS: 50%",0)
			lcd_show("DESEA CAMBIAR EL",1)
			lcd_show("NIVEL DE APERTURA?",2)
			lcd_show("SI        NO",3)
	
			
			if  buton4.value() is 0:
				horario_programado()
				lcd_clear()
				lcd_show("ELIJA EL NIVEL DE",0)
				lcd_show("APERTURA DESEADO",1)
				sleep(3)
				lcd_clear()
				lcd_show("USE EL BOTON ARRIBA",0)
				lcd_show("  Y ABAJO PARA",1)
				lcd_show("  DESPLAZARSE",2)
				sleep(3)
				lcd_clear()
			
				result2=todo50()
				
				i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				
				valor = result2
				valor2 = grados
				data  = [{label: valor}, 
				{label2: valor2}]
				publish_thingsboard(red,clave,token, unique_id,data)
				sleep(3)
				horario_programado()
				
			elif buton2.value() is 0:
				lcd_clear()
				sleep(2)
				horario_programado()
				break
	    	
			else:
				continue
			break
			
				
		elif (grados > 45) and (grados <= 68):	
			horario_programado()
			lcd_show("ABIERTAS: 75%",0)
			lcd_show("DESEA CAMBIAR EL",1)
			lcd_show("NIVEL DE APERTURA?",2)
			lcd_show("SI        NO",3)
	
			
			if  buton4.value() is 0:
				horario_programado()
				lcd_clear()
				lcd_show("ELIJA EL NIVEL DE",0)
				lcd_show("APERTURA DESEADO",1)
				sleep(3)
				lcd_clear()
				lcd_show("USE EL BOTON ARRIBA",0)
				lcd_show("  Y ABAJO PARA",1)
				lcd_show("  DESPLAZARSE",2)
				sleep(3)
				lcd_clear()
				
				result2=todo75()
				
				i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				
				valor = result2
				valor2 = grados
				data  = [{label: valor}, 
				{label2: valor2}]
				publish_thingsboard(red,clave,token, unique_id,data)
				sleep(3)
				
			elif buton2.value() is 0:
				lcd_clear()
				sleep(2)
				horario_programado()
				break
	    	
			else:
				continue
			break
			
			
		elif (grados > 88) and (grados <= 91):
			horario_programado()	
			lcd_show("ABIERTAS: 100%",0)
			lcd_show("DESEA CAMBIAR EL",1)
			lcd_show("NIVEL DE APERTURA?",2)
			lcd_show("SI        NO",3)
	
			
			if  buton4.value() is 0:
				lcd_clear()
				lcd_show("ELIJA EL NIVEL DE",0)
				lcd_show("APERTURA DESEADO",1)
				sleep(3)
				lcd_clear()
				lcd_show("USE EL BOTON ARRIBA",0)
				lcd_show("  Y ABAJO PARA",1)
				lcd_show("  DESPLAZARSE",2)
				sleep(3)
				lcd_clear()
				
				result2=todo100()
				
				i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				
				valor = result2
				valor2 = grados
				data  = [{label: valor}, 
				{label2: valor2}]
				publish_thingsboard(red,clave,token, unique_id,data)
				sleep(3)
				
			elif buton2.value() is 0:
				lcd_clear()
				sleep(2)
				horario_programado()
				break
	    	
			else:
				continue
			break
			
			
		elif grados == 0:
			lcd_show("VENTILAS CERRADAS",0)
			lcd_show("   ABRIR?",1)
			lcd_show("SI        NO",3)
	
			if  buton4.value() is 0:
				horario_programado()
				lcd_clear()
				lcd_show("ELIJA EL NIVEL DE",0)
				lcd_show("APERTURA DESEADO",1)
				sleep(3)
				lcd_clear()
				lcd_show("USE EL BOTON ARRIBA",0)
				lcd_show("  Y ABAJO PARA",1)
				lcd_show("  DESPLAZARSE",2)
				sleep(3)
				lcd_clear()
				
				result2=todocero()

				i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				
				valor = result2
				valor2 = grados
				data  = [{label: valor}, 
				{label2: valor2}]
				publish_thingsboard(red,clave,token, unique_id,data)
				sleep(3)
				
		 		horario_programado()
		 		
			elif buton2.value() is 0:
				lcd_clear()
				sleep(2)
				
				horario_programado()
				break
	    	
			else:
				continue
			break
			
			
		elif (grados < 0):
			horario_programado()
			lcd_clear()
			lcd_show(" APERTURA FUERA DE",0)
			lcd_show("      RANGO!",1)
			sleep(3)
			lcd_clear()
			lcd_show(" AJUSTE LA POSICION",1)
			lcd_show(" DEL ACELEROMETRO",2)
			sleep(5)
			lcd_clear()
			break
			
		elif (grados > 91):
			horario_programado()
			lcd_clear()
			lcd_show(" APERTURA FUERA DE",0)
			lcd_show("      RANGO!",1)
			sleep(3)
			lcd_clear()
			lcd_show(" AJUSTE LA POSICION",1)
			lcd_show(" DEL ACELEROMETRO",2)
			sleep(5)
			lcd_clear()
			break

    
		
	

        

