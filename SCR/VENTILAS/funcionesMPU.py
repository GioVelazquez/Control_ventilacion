# - SISTEMA DE CONTROL DE VENTILAS -

# POR: GIOVANNI VELAZQUEZ AVILEZ
# ESTUDIANTE DEL ITZ DE ING ELECTROMECANICA
# RESIDENTE EN EL IER-UNAM, AGO-DIC 2020

from machine import I2C, Pin
from time import sleep
import time
import math
import machine
import utime


MPU6050_ADDR = 0x68

MPU6050_ACCEL_XOUT_H = 0x3B
MPU6050_ACCEL_XOUT_L = 0x3C
MPU6050_ACCEL_YOUT_H = 0x3D
MPU6050_ACCEL_YOUT_L = 0x3E
MPU6050_ACCEL_ZOUT_H = 0x3F
MPU6050_ACCEL_ZOUT_L = 0x40
MPU6050_TEMP_OUT_H = 0x41
MPU6050_TEMP_OUT_L = 0x42
MPU6050_GYRO_XOUT_H = 0x43
MPU6050_GYRO_XOUT_L = 0x44
MPU6050_GYRO_YOUT_H = 0x45
MPU6050_GYRO_YOUT_L = 0x46
MPU6050_GYRO_ZOUT_H = 0x47
MPU6050_GYRO_ZOUT_L = 0x48
MPU6050_PWR_MGMT_1 = 0x6B

MPU6050_LSBC = 340.0
MPU6050_TEMP_OFFSET = 36.53
MPU6050_LSBG = 16384.0
MPU6050_LSBDS = 131.0

RestrictPitch = True	
radToDeg = 57.2957786

def mpu6050_init(i2c):
    i2c.writeto_mem(MPU6050_ADDR, MPU6050_PWR_MGMT_1, bytes([0]))


def combine_register_values(h, l):
    if not h[0] & 0x80:
        return h[0] << 8 | l[0]
    return -((h[0] ^ 255) << 8) |  (l[0] ^ 255) + 1

def mpu6050_get_accel(i2c):
    accel_x_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_XOUT_H, 1)
    accel_x_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_XOUT_L, 1)
    accel_y_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_YOUT_H, 1)
    accel_y_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_YOUT_L, 1)
    accel_z_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_ZOUT_H, 1)
    accel_z_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_ZOUT_L, 1)
    
    return [combine_register_values(accel_x_h, accel_x_l) / MPU6050_LSBG,
            combine_register_values(accel_y_h, accel_y_l) / MPU6050_LSBG,
            combine_register_values(accel_z_h, accel_z_l) / MPU6050_LSBG]
            

def mpu6050_get_accel_angle_zy(i2c):
	accel_x_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_XOUT_H, 1)
	accel_x_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_XOUT_L, 1)
	a= combine_register_values(accel_x_h, accel_x_l) / MPU6050_LSBG
	
	accel_y_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_YOUT_H, 1)
	accel_y_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_YOUT_L, 1)
	b= combine_register_values(accel_y_h, accel_y_l) / MPU6050_LSBG

	accel_z_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_ZOUT_H, 1)
	accel_z_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_ZOUT_L, 1)
	c= combine_register_values(accel_z_h, accel_z_l) / MPU6050_LSBG
	
	if (RestrictPitch):
		roll = math.atan2(b, c) * radToDeg
    		pitch = math.atan(-a/math.sqrt((b**2)+(c**2))) * radToDeg
	else:
		
    		roll = math.atan(b/math.sqrt((a**2)+(c**2))) * radToDeg
    		pitch = math.atan2(-a,c) * radToDeg
	
	return int(roll)

	
def mpu6050_get_accel_angle_zx(i2c):
	accel_x_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_XOUT_H, 1)
	accel_x_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_XOUT_L, 1)
	x= combine_register_values(accel_x_h, accel_x_l) / MPU6050_LSBG
	
	accel_y_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_YOUT_H, 1)
	accel_y_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_YOUT_L, 1)
	y= combine_register_values(accel_y_h, accel_y_l) / MPU6050_LSBG

	accel_z_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_ZOUT_H, 1)
	accel_z_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_ZOUT_L, 1)
	z= combine_register_values(accel_z_h, accel_z_l) / MPU6050_LSBG
	
	if (RestrictPitch):
		roll = math.atan2(x, z) * radToDeg
    		pitch = math.atan(-y/math.sqrt((x**2)+(z**2))) * radToDeg
	else:
		
    		roll = math.atan(x/math.sqrt((y**2)+(z**2))) * radToDeg
    		pitch = math.atan2(-y,z) * radToDeg
	
	return int(roll)	

if __name__ == "__main__":
    i2c = I2C(scl=Pin(12), sda=Pin(14))
    mpu6050_init(i2c)
    
    while True:
	
	#print("Acelerometro:\t", mpu6050_get_accel(i2c), "g")
	#print("Angulo zy:\t", mpu6050_get_accel_angle_zy(i2c),"°")
	print("Angulo zx:\t", mpu6050_get_accel_angle_zx(i2c),"°")
	time.sleep(1)
        
	





