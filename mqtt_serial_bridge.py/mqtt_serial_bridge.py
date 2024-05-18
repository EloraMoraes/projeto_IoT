import serial
import time
import paho.mqtt.client as mqtt

# Configurações da porta serial
ser = serial.Serial('COM5', 9600)  # Substitua 'COM4' pela porta correta no seu computador
time.sleep(2)  # Aguarda a inicialização da comunicação serial

# Configurações do MQTT
broker = "broker.hivemq.com"
port = 1883
topic = "sensor/temperature"

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Conectado com código " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)
client.loop_start()

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print("Lido do Arduino: " + line)
            if line.startswith("Temperatura:"):
                temperature = line.split()[1]
                client.publish(topic, temperature)
                print("Publicado no MQTT: " + temperature)
        time.sleep(1)
except KeyboardInterrupt:
    print("Saindo...")
finally:
    ser.close()
    client.loop_stop()
    client.disconnect()
