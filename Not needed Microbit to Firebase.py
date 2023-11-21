#The Microbit Serial
import serial
import serial.tools.list_ports as list_ports
import time
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

#File Address
cred = credentials.Certificate("C:\\Users\\18MMcLynn.ACC\\Desktop\\Python\\Firebase\\microbit-75378-firebase-adminsdk-je0pw-1b6a0a95b6.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://microbit-75378-default-rtdb.europe-west1.firebasedatabase.app/'})

PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.1

#Looks for Port
def find_comport(pid, vid, baud):
    ''' return a serial port '''
    ser_port = serial.Serial(timeout=TIMEOUT)
    ser_port.baudrate = baud
    ports = list(list_ports.comports())
    #print('scanning ports')
    for p in ports:
        if (p.pid == pid) and (p.vid == vid):
            #print('found target device pid: {} vid: {} port: {}'.format(
            #    p.pid, p.vid, p.device))
            ser_port.port = str(p.device)
            return ser_port
    return None


#Microbit Data to FireBase
print('intializing microbit data')
ser_micro = find_comport(PID_MICROBIT, VID_MICROBIT, 115200)
if not ser_micro:
    print('error, microbit not detected')
else:
    print("Microbit Found")
    ser_micro.open()
    source = "Microbit"
    i = 0
    ref = db.reference().child('temp_log')
    while True:
        data = str(ser_micro.readline().decode('utf-8'))
        data = data.replace(" ","")
        data = data.replace("\r\n","")
    
        if data.isdigit():
            ref.update({str(int(time.time())):{'Temp':data, 'Location':source}})
            i = i + 1
            print(data)
        else:
            rands = 0
            rands = rands + 1
        #time.sleep(5)
        
        
#Old Junk
'''
ref = db.reference()
ref.update({'':''})
f=ref = db.reference().child (input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(DigitalPin.P2, 1)
}))
'''