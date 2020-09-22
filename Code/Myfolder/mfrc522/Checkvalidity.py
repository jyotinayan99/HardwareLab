import buzzer

#Checkvalidity

def Checkvaildity(data):
    conn = None
    try:
        conn = sqlite3.connect("mydb.db")
        cur = conn.cursor()
        cur.execute("select * from mytable")
        result = cur.fetchall()

        cnt=0
        arr = []
        for i in range(len(result)):
            arr.append(result[i][0])

        fgl=False
        mydat=str(data)
        
        if mydat in arr:
            fgl=True

        if fgl==False:
            buzzer.beep_buzz()
        else:
            print("Recognized " + str(mydat))
        return fgl

    except:
        print('Exception')
    return False


#end of Checkvalidity