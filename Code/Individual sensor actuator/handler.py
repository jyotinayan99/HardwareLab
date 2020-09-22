import RPi.GPIO as GPIO
import time
import SimpleMFRC522
import paho.mqtt.client as mqtt
import sqlite3

from keypad import keypad


def handler():

    mqttfunc(txt, 'open', 0, 0)
    kp = keypad(columnCount=3)
    print("Enter the amount of items inserted")
    
    digit1 = None
    while digit1 == None:
        digit1 = kp.getKey()
        time.sleep(0.2)
    digit2 = None
    while digit2 == None:
        digit2 = kp.getKey()
        time.sleep(0.2)
    digit3 = None
    while digit3 == None:
        digit3 = kp.getKey()
        time.sleep(0.2)
    
    try:
        conn = sqlite3.connect("mydb.db")
        print("Connected to database")
        cur = conn.cursor()
        cur.execute("SELECT * FROM counttable")
        res = cur.fetchall()

        for i in res:
            print(i)
        print("values of counttable")
        v1 = int(res[0][1])
        v2 = int(res[0][2])
        v3 = int(res[0][3])
        
        
        cur.execute("UPDATE counttable SET count1 = ?, count2 = ?, count3 = ? WHERE pkey=1;", (digit1,digit2,digit3) )
        conn.commit()
        
        cur.execute("Select * from counttable")
        result = cur.fetchall()
        for i in result:
            print(i)
        mqttfunc(txt, 'close', 0, 0)
        
    except:
        print("Error in Setting Data")


#end of handler function