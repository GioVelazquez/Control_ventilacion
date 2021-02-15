# - SISTEMA DE MEDICION DE VENTANA DESLIZABLE -

# CODIGO DE APOYO 
# PROPORCIONADO EN TALLER IOT DEL IER-UNAM 
import math
from umqtt.simple import MQTTClient
import gc
import json
import machine, time
from wifi import do_connect

def settimeout(duration):
  pass
def t3_publication(topic, msg):
  print (topic, ';', msg)
  pycom.rgbled(0xff00)

def publish_thingsboard(red, clave,token,UNIQUE_ID,data):

  contador = 0
  condicion = True
  while condicion:
      try:
          client = MQTTClient(UNIQUE_ID, "iot.ier.unam.mx", port = 1883, user=token, password='')
          client.settimeout = settimeout
          client.connect()
          print(json.dumps(data))
          client.publish('v1/devices/me/telemetry', json.dumps(data) )
          client.disconnect()
          condicion = False
      except Exception as inst:
          do_connect(red,clave);
          time.sleep(10)
          contador += 1
          print("Falla ",contador)
          if contador >= 10:
              machine.reset()


