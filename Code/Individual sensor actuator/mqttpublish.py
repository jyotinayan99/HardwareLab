#mqtt publish

import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def mqttfunc(txt,val1,val2,val3):
    try:
        client=mqtt.Client()
        client.username_pw_set("dcbqmxgj","pDywpQtuo59T")
        client.connect("m14.cloudmqtt.com",12109,60)
        if str(txt).strip() == 'Handler':
            client.publish('tt', '%s %s %d %d' % ('Handler',val1,val2,val3))
        else:
            client.publish('tt', '%s %d %d %d' %(txt,val1,val2,val3))
    except:
        print("Mqtt error")

#end of mqtt publish
