import RPi.GPIO as GPIO
import time
import SimpleMFRC522
import paho.mqtt.client as mqtt
import sqlite3

from keypad import keypad




import buzzer
import mqttpublish
import Checkvalidity
import servomotor
import stepmotor
import handler

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



reader = SimpleMFRC522.SimpleMFRC522()
print("Code Initiated")
i=0;

    

def Readcard():
    print("Scannig for a ID")
    ida,text = reader.read()
    return ida,text

    


try:
    while True:

        conn = sqlite3.connect("mydb.db")
        print("Connected to database")
        cur = conn.cursor()
        cur.execute("Select * from counttable")
        res = cur.fetchall()
        for i in res:
            print(i)
        v1 = int(res[0][1])
        v2 = int(res[0][2])
        v3 = int(res[0][3])

        if(v1<2 or v2<2 or v3<2):
            print('LOW NUMBERS OF ITEMS AVAILABLE')
        
        id, txt = reader.read()

        if not Checkvalidity.Checkvalidity(txt):
            buzzer.beep_buzz()
            continue
        
 
        if str(txt).strip() == "Handler":
            handler.handler()
            continue
        else:
            kp = keypad(columnCount = 3)
            print(str(txt).strip())
            print("Please Enter the number of items of each type")
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
            
            conn = sqlite3.connect("mydb.db")
            print("Connected to database")
            cur = conn.cursor()
            cur.execute("Select * from counttable")
            res = cur.fetchall()
            print("Counttabkle")
            for i in res:
                print(i)
            
            v1 = int(res[0][1])
            v2 = int(res[0][2])
            v3 = int(res[0][3])

            if(digit1>v1 or digit2>v2 or digit3>v3):
                print("Requested number of items not available")
                continue

            print("Entered digits are:")
            print(digit1)
            print(digit2)
            print(digit3)
        
            mqttpublish.mqttfunc(txt,digit1,digit2,digit3)
            
            conn = None

            if(digit1!=0):
                stepmot.stepmot(2,digit1)
            if(digit2!=0):
                stepmot.stepmot(1,digit2)
                
            conn = sqlite3.connect("mydb.db")
            print("Connected to database")
            cur = conn.cursor()
            cur.execute("Select * from counttable")
            res = cur.fetchall()
            for i in res:
                print(i)
            v1 = int(res[0][1])-int(digit1)
            v2 = int(res[0][2])-int(digit2)
            v3 = int(res[0][3])-int(digit3)
            print(v1)
            print(v2)
            print(v3)
            cur.execute("UPDATE counttable SET count1 = ?, count2 = ?, count3 = ? WHERE pkey=1;", (v1,v2,v3) )
            conn.commit()
        
            cur.execute("Select * from counttable")
            
            result = cur.fetchall()
            for i in result:
                print(i)

            
            cur.execute("UPDATE mytable SET isissued= 0, val1 =?, val2 = ?, val3 = ? WHERE rfid = ?;", (digit1, digit2, digit3, txt) )
            conn.commit()

            i=0
        
            
finally:
	GPIO.cleanup()

