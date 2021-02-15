# - SISTEMA DE MEDICION DE VENTANA DESLIZABLE -

# POR: GIOVANNI VELAZQUEZ AVILEZ
# ESTUDIANTE DEL ITZ DE ING ELECTROMECANICA
# RESIDENTE EN EL IER-UNAM, AGO-DIC 2020

import machine
import time
import gc
import network, utime, ntptime
from machine import Pin, DAC, I2C
import funcionesMPU
from funcionesMPU import *
from time import sleep 
from wifi import activate_wifi
import esp8266_i2c_lcd
from esp32_i2c_lcd import I2cLcd 
from lcd_api import LcdApi

# LCD 2004 I2C: Vcc -> 5V, Gnd -> G, SCL -> D1,  SDA -> D2
lcd = I2cLcd(I2C(scl=Pin(26), sda=Pin(13)), 0x27, 4, 20)

red = 'TOTALPLAY_897E2E'
clave = 'EZ04022ST1'

label ='modulacion'
label2='inclinacion'

web_query_delay = 600000
timezone_hour = 6 # ZONA HORARIA (hours)

alarm = [11, 30] # ALARMA[HORA, MINUTO]
alarm2 = [11, 56] # ALARMA[HORA, MINUTO]


dac1=DAC(Pin(25))
led = Pin(27, Pin.OUT)
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

def nivel1():
	print ('-------> CERRANDO VENTILAS <-------')
    	lcd_show("CERRANDO VENTILAS",1)
        #Parpadea el LED

	led.value(1)
	utime.sleep(0.1)
	led.value(0)
	utime.sleep(0.1)
	led.value(1)
	utime.sleep(0.1)
	led.value(0)
	volts = 2
	dac1.write(44)
	sleep(10)
	dac1.write(0)
	sleep(1)
	return volts


def nivel2():
	print ('-------> ABRIENDO 25% <-------')
    	lcd_show("ABRIENDO 25%",1)
        #Parpadea el LED
	led.value(1)
	utime.sleep(0.1)
	led.value(0)
	utime.sleep(0.1)
	led.value(1)
	utime.sleep(0.1)
	led.value(0)
	volts = 3
	dac1.write(70)
	sleep(10)
	dac1.write(0)
	sleep(1)
	return volts

def nivel3():
	print ('-------> ABRIENDO 50% <-------')
    	lcd_show("ABRIENDO 50%",1)
        #Parpadea el LED
	led.value(1)
	utime.sleep(0.1)
	led.value(0)
	utime.sleep(0.1)
	led.value(1)
	utime.sleep(0.1)
	led.value(0)
	volts = 4
	dac1.write(96)
	sleep(10)
	dac1.write(0)
	sleep(1)
	return volts


def nivel4():

	print ('-------> ABRIENDO 75% <-------')
    	lcd_show("ABRIENDO 75%",1)
        #Parpadea el LED

	led.value(1)
	utime.sleep(0.1)
	led.value(0)
	utime.sleep(0.1)
	led.value(1)
	utime.sleep(0.1)
	led.value(0)
	
	volts = 5.03
	dac1.write(123)
	sleep(10)
	dac1.write(0)
	sleep(1)
	return volts


def nivel5():
	print ('-------> ABRIENDO 100% <-------')
    	lcd_show("ABRIENDO 100%",1)
        #Parpadea el LED
	led.value(1)
	utime.sleep(0.1)
	led.value(0)
	utime.sleep(0.1)
	led.value(1)
	utime.sleep(0.1)
	led.value(0)
	
	volts = 6.01
	dac1.write(150)
	sleep(10)
	dac1.write(0)
	sleep(1)
	return volts
	
def todo25():
	A = int
	A = 1
	while True:	
		if buton3.value() is 0:
			A +=1				
		if buton1.value() is 0:
			A -=1				
		if A > 4:
			A = 1						
		if A == 1 :			
			lcd_clear()
			lcd_show("CERRAR <------ ",0)
			lcd_show("50%",1)
			lcd_show("75%",2)
			lcd_show("100%",3)
			if  buton4.value() is 0:
	    			lcd_clear()
	    			result=nivel1()
	    			lcd_clear()
	    			i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados == 0:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					lcd_clear()
					lcd_show(" {} GRADOS ".format(grados) , 1)
					sleep(3)
					continue
		    		break
		    	else:
				continue
		    	break
		    			
	    	
		if A == 2 :
						
			lcd_clear()
			lcd_show("CERRAR",0)
			lcd_show("50% <------ ",1)
			lcd_show("75%",2)
			lcd_show("100%",3)
			#utime.sleep_ms(200)
			if  buton4.value() is 0:
				lcd_clear()
	  			
	  			result=nivel3()
	    			lcd_clear()
	    			i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados >= 44 and grados <=46:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		    	else:
				continue
		    	break
	    		
		if A == 3 :
						
			lcd_clear()
			lcd_show("CERRAR",0)
			lcd_show("50%",1)
			lcd_show("75% <------",2)
			lcd_show("100%",3)
		    	#utime.sleep_ms(200)
		    			
			if  buton4.value() is 0:
				lcd_clear()
		    		
		    		result=nivel4()
		    		lcd_clear()
		    		i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados >= 66 and grados <=68:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		    	else:
				continue
		    	break
		    	
		if A == 4 :
						
			lcd_clear()
			lcd_show("CERRAR",0)
			lcd_show("50%",1)
			lcd_show("75%",2)
			lcd_show("100% <------",3)
			#utime.sleep_ms(200)
					
			if  buton4.value() is 0:
		    		lcd_clear()
		    		
		    		result=nivel5()
		    		lcd_clear()
		    		i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados >= 89 and grados <=91:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		    	else:
				continue
		    	break
		    

	return result	
		
def todo50():
	A = int
	A = 1	
			
	while True:			
		if buton3.value() is 0:
			A +=1
						
		if buton1.value() is 0:
			A -=1
						
		if A > 4:
			A = 1
					
					
		if A == 1 :
						
			lcd_clear()
			lcd_show("CERRAR <------ ",0)
			lcd_show("25%",1)
			lcd_show("75%",2)
			lcd_show("100%",3)
			#utime.sleep_ms(200)
			if  buton4.value() is 0:
	    			lcd_clear()
	    			result=nivel1()
	    			lcd_clear()
	    			i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados == 0:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		    	else:
				continue
		    	break
	    		
	    	
	    	if A == 2 :
						
			lcd_clear()
			lcd_show("CERRAR",0)
			lcd_show("25% <------ ",1)
			lcd_show("75%",2)
			lcd_show("100%",3)
			#utime.sleep_ms(200)
			if  buton4.value() is 0:
				lcd_clear()
	  			result=nivel2()
	    			lcd_clear()
	    			i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados >= 21 and grados <=23:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		    	else:
				continue
		    	break
	    		
		    			
		if A == 3 :
						
			lcd_clear()
			lcd_show("CERRAR",0)
			lcd_show("25%",1)
			lcd_show("75% <------",2)
			lcd_show("100%",3)
		    	#utime.sleep_ms(200)
		    			
			if  buton4.value() is 0:
				lcd_clear()
		    		result=nivel4()
		    		lcd_clear()
		    		i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados >= 66 and grados <=68:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		    	else:
				continue
		    	break
		    		
		    	
		if A == 4 :
						
			lcd_clear()
			lcd_show("CERRAR",0)
			lcd_show("25%",1)
			lcd_show("75%",2)
			lcd_show("100% <------",3)
			#utime.sleep_ms(200)
					
			if  buton4.value() is 0:
		    		lcd_clear()
		    		result=nivel5()
		    		lcd_clear()
		    		i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados >= 89 and grados <=91:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		    	else:
				continue
		    	break
		    		    
	return result				
						
def todo75():
	A = int
	A = 1	
	
	while True:			
		if buton3.value() is 0:
			A +=1
						
		if buton1.value() is 0:
			A -=1
						
		if A > 4:
			A = 1
					
					
		if A == 1 :
						
			lcd_clear()
			lcd_show("CERRAR <------ ",0)
			lcd_show("25%",1)
			lcd_show("50%",2)
			lcd_show("100%",3)
			#utime.sleep_ms(200)
			if  buton4.value() is 0:
		    		lcd_clear()
		    		result=nivel1()
		    		lcd_clear()
		    		i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados == 0:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		    	else:
				continue
		    	break
		    
		    			
	    	
	    	if A == 2 :
						
			lcd_clear()
			lcd_show("CERRAR",0)
			lcd_show("25% <------ ",1)
			lcd_show("50%",2)
			lcd_show("100%",3)
			#utime.sleep_ms(200)
			if  buton4.value() is 0:
				lcd_clear()
	  			result=nivel2()
	    			lcd_clear()
	    			i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados >= 21 and grados <=23:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		    	else:
				continue
		    	break
	    		
		    			
		if A == 3 :
						
			lcd_clear()
			lcd_show("CERRAR",0)
			lcd_show("25%",1)
			lcd_show("50% <------",2)
			lcd_show("100%",3)
		    	#utime.sleep_ms(200)
		    			
			if  buton4.value() is 0:
				lcd_clear()
		    		result=nivel3()
		    		lcd_clear()
		    		i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados >= 44 and grados <=46:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		    	else:
				continue
		    	break
		    	
		if A == 4 :
						
			lcd_clear()
			lcd_show("CERRAR",0)
			lcd_show("25%",1)
			lcd_show("50%",2)
			lcd_show("100% <------",3)
			#utime.sleep_ms(200)
					
			if  buton4.value() is 0:
		    		lcd_clear()
		    		result=nivel5()
		    		lcd_clear()
		    		i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados >= 89 and grados <=91:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		    	else:
				continue
		    	break
		    	
	return result
			
def todo100():
	A = int
	A = 1	
	
	while True:			
		if buton3.value() is 0:
			A +=1
						
		if buton1.value() is 0:
			A -=1
						
		if A > 4:
			A = 1
					
					
		if A == 1 :
						
			lcd_clear()
			lcd_show("CERRAR <------ ",0)
			lcd_show("25%",1)
			lcd_show("50%",2)
			lcd_show("75%",3)
			#utime.sleep_ms(200)
			if  buton4.value() is 0:
		    		lcd_clear()
		    		result=nivel1()
		    		lcd_clear()
		    		i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados == 0:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		    	else:
				continue
		    	break
		   
	    	
	    	if A == 2 :
						
			lcd_clear()
			lcd_show("CERRAR",0)
			lcd_show("25% <------ ",1)
			lcd_show("50%",2)
			lcd_show("75%",3)
			#utime.sleep_ms(200)
			if  buton4.value() is 0:
				lcd_clear()
	  			result=nivel2()
	    			lcd_clear()
	    			i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados >= 21 and grados <=23:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		    	else:
				continue
		    	break
	    		
		    			
		if A == 3 :
						
			lcd_clear()
			lcd_show("CERRAR",0)
			lcd_show("25%",1)
			lcd_show("50% <------",2)
			lcd_show("75%",3)
		    	#utime.sleep_ms(200)
		    			
			if  buton4.value() is 0:
				lcd_clear()
		    		result=nivel3()
		    		lcd_clear()
		    		i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados >= 44 and grados <=46:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		    	else:
				continue
		    	break
		    	
		if A == 4 :
						
			lcd_clear()
			lcd_show("CERRAR",0)
			lcd_show("25%",1)
			lcd_show("50%",2)
			lcd_show("75% <------",3)
			#utime.sleep_ms(200)
					
			if  buton4.value() is 0:
		    		lcd_clear()
		    		result=nivel4()
		    		lcd_clear()
		    		i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados >= 66 and grados <=68:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		    	else:
				continue
		    	break
		        
	return result
	
def todocero():
	A = int
	A = 1
			
	while True:			
		if buton3.value() is 0:
			A +=1
						
		if buton1.value() is 0:
			A -=1
						
		if A > 4:
			A = 1
					
					
		if A == 1 :
				
			lcd_clear()
			lcd_show("25% <------ ",0)
			lcd_show("50%",1)
			lcd_show("75%",2)
			lcd_show("100%",3)
			#utime.sleep_ms(200)
			if  buton4.value() is 0:
		    		lcd_clear()
		    		result=nivel2()
		    		lcd_clear()
		    		i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados >=21 and grados <=23:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					lcd_clear()
					lcd_show(" {} GRADOS ".format(grados) , 1)
					sleep(3)
					continue
				
		    		break
		    	else:
				continue
		    	break

		    			
	    	
	    	if A == 2 :
						
			lcd_clear()
			lcd_show("25%",0)
			lcd_show("50% <------ ",1)
			lcd_show("75%",2)
			lcd_show("100%",3)
			#utime.sleep_ms(200)
			if  buton4.value() is 0:
				lcd_clear()
	  			result=nivel3()
	    			lcd_clear()
	    			i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados >= 44 and grados <=46:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		    	else:
				continue
		    	break
	    	
		if A == 3 :
						
			lcd_clear()
			lcd_show("25%",0)
			lcd_show("50%",1)
			lcd_show("75% <------",2)
			lcd_show("100%",3)
		    	#utime.sleep_ms(200)
		    			
			if  buton4.value() is 0:
				lcd_clear()
		    		result=nivel4()
		    		lcd_clear()
		    		i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados >= 66 and grados <=68:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		else:
			continue
		break
		    	
		if A == 4 :
						
			lcd_clear()
			lcd_show("25%",0)
			lcd_show("50%",1)
			lcd_show("75%",2)
			lcd_show("100% <------",3)
			#utime.sleep_ms(200)
					
			if  buton4.value() is 0:
		    		lcd_clear()
		    		result=nivel5()
		    		lcd_clear()
		    		i2c = I2C(scl=Pin(12), sda=Pin(14))
		    		mpu6050_init(i2c)
				grados=mpu6050_get_accel_angle_zx(i2c)
				sleep(1)
				if grados >= 89 and grados <=91:
					lcd_show(" OPERACION EXITOSA ",1)
					sleep(2)
					lcd_clear()
				else:
					continue
				
		    		break
		else:
			continue
		break
		    	
	return result
	
def horario_programado():
	local_time_sec = utime.time() + timezone_hour * 3600
	local_time = utime.localtime(local_time_sec)
	update_time = utime.ticks_ms() - web_query_delay
	
	ntptime.settime()
	print("HORA DEL SISTEMA ACTUALIZADO:", utime.localtime())
	update_time = utime.ticks_ms()
		
		
	if alarm[0] == local_time[3] and alarm[1] == local_time[4]:
        
        	print("!!! HORA PROGRAMADA !!!")
      		lcd_clear()
      		lcd_show("    10:00 PM   ",0)
		lcd_show("HORARIO PROGRAMADO",1)
		lcd_show("   DE APERTURA",2)
		sleep(5)
		lcd_clear()	
		nivel5()	
		lcd_clear()
		lcd_show("ESPERE UN MOMENTO...",2)
		sleep(30)
		lcd_clear()
		i2c = I2C(scl=Pin(12), sda=Pin(14))
		mpu6050_init(i2c)
		grados=mpu6050_get_accel_angle_zx(i2c)
		sleep(1)
		if grados >= 88 and grados <=91:
			lcd_show(" OPERACION EXITOSA ",1)
			sleep(5)
			lcd_clear()
			
		else:
			lcd_clear()
			lcd_show(" {} GRADOS ".format(grados) , 1)
			sleep(5)
			brea
			
    
    	elif alarm2[0] == local_time[3] and alarm2[1] == local_time[4]:
    		print("!!! HORA PROGRAMADA !!!")
		lcd_clear()
        	lcd_show("    07:00 AM   ",0)
		lcd_show("HORARIO PROGRAMADO",1)
		lcd_show("   DE CIERRE",2)
		sleep(5)
		lcd_clear()
		nivel1()
		lcd_clear()
		lcd_show("ESPERE UN MOMENTO...",2)
		sleep(30)
		lcd_clear()
		i2c = I2C(scl=Pin(12), sda=Pin(14))
		mpu6050_init(i2c)
		grados=mpu6050_get_accel_angle_zx(i2c)
		sleep(1)
		if grados == 0:
			lcd_show(" OPERACION EXITOSA ",1)
			sleep(5)
			lcd_clear()
			
		else:
			lcd_clear()
			lcd_show(" {} GRADOS ".format(grados) , 1)
			sleep(5)
			

