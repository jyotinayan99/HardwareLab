import RPi.GPIO as GPIO
import time
import SimpleMFRC522

import mysql.connector
from keypad import keypad

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

reader = SimpleMFRC522.SimpleMFRC522()
print("jshdf")
i=0;

def Readcard():
    print("Scannig for a rfid")
    ida,text = reader.read()
    return ida,text

def Checkvaliddata(idin,namein):
    f = open('doc','r')
    for line in f:
        for word in line.split():
            if word.isnumeric():
                ida = word
            else:
                name = word
        if ida==idin and name==namein:
            return 1
    return 0;
    
def beep_buzz():
    GPIO.output(18,true)
    time.sleep(0.5)
    GPIO.output(18,False)
    return;
try:
    while i==0:
	id, text = reader.read()
	print(id)
	print(text+"fgh")
	i=1;
	#GPIO.output(18, False)
	validity = Checkvaliddata(ida,text)
	if(validity!=1):
            print("Unauthorized access")
            i=0
            continue
	kp = keypad(columnCount = 4)
	print("Waiting for keypress")
        # waiting for a keypress
        digit = None
        while digit == None:
            digit = kp.getKey()
        # Print result
        #print digit
        #time.sleep(0.5)
     
        ###### 4 Digit wait ######
        #seq = []
        #for i in range(4):
        #    digit = None
            """while digit == None:
                digit = kp.getKey()
            seq.append(digit)
            time.sleep(0.4)
     
        # Check digit code
        print(seq)
        if seq == [1, 2, 3, '#']:
            print "Code accepted"
            """
        
        if(digit!=1 and digit!=2 and digit!=3):
            print("Invalid num")
        if(digit==1):
            print("s")
            
finally:
	GPIO.cleanup()
