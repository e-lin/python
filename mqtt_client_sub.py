# encoding: utf-8
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code"+str(rc))
    client.subscribe("hello/proxy")

def on_message(client, userdata, msg):
    print "Topic:", msg.topic+'\nMessage:'+str(msg.payload)
    client.loop_stop()
    # Call external command while receiving data from the mqtt broker.
    from subprocess import call
    call(["ls", "-al"])
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()