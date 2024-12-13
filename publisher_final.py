import paho.mqtt.client as mqtt
import time
import random
import psutil as ps
import json

cliente = mqtt.Client()                 # Cria um cliente MQTT
cliente.connect("test.mosquitto.org")   # Conecta ao broker

while True:
##aquisições
  cpu_use = ps.cpu_percent()
  ram_use = ps.virtual_memory().percent
  cpu_bat = ps.sensors_battery() #nootebook
  cpu_freq = ps.cpu_freq()
  disco = ps.disk_usage('c:')
  payload = [
    cpu_use,
    ram_use,
    cpu_bat[0],
    cpu_bat[2],
    cpu_freq[0],
    cpu_freq[2],
    disco[0],
    disco[1],
    disco[2],
    disco[3],]
  json_payload = json.dumps(payload)

  ##publicar
  cliente.publish("UFSC/DAS/NEMO",json_payload)  # Publica o valor no tópico especificado
  time.sleep(5)  