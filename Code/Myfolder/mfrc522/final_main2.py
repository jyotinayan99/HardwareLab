import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



import servomotor
import stepmotor


    
def myfunc(text_parts):
    stepmotor.stepmot(3,text_parts[3])
    
def on_connect ( client, userdata, flags, rc):
    print("Connected with code :" +str(rc))
    client.subscribe("tt/#")
    
def on_message ( client, userdata, msg):
    tpc = str(msg.topic)
    
    text = str(msg.payload)
    n = len(text)
    
    text_parts = text.split()
    for i in text_parts:
        print(i)
    if(str(text_parts[1]).strip() == "close"):
        resetmotor()
    cnt = int(text_parts[3])
    slpval=0
    if not str(text_parts[1]).isalpha():
        slpval= (4.6*(int(text_parts[1])+int(text_parts[2])))

    if(text_parts[0] == "Handler"):
        if(str(text_parts[1]).strip() == "open"):
            rotatemotor()
            
            return
        if(str(text_parts[1]).strip() == "close"):
           resetmotor()
        cnt=0
        slpval=0
        
    time.sleep(slpval)
    stepmot.stepmotor(3,cnt)


    
client = mqtt.Client()
client.on_connect = on_connect 
client.on_message = on_message


client.username_pw_set("dcbqmxgj", "pDywpQtuo59T")
client.connect("m14.cloudmqtt.com",12109,60)

client.loop_forever()

