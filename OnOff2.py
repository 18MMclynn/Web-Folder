#The Microbit Serial
import serial
import serial.tools.list_ports as list_ports
import time
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
def doSomething(response):
    print(response.data)
#File Address
cred = credentials.Certificate("C:\\Users\\18MMcLynn.ACC\\Desktop\\Python\\Firebase\\microbit-75378-firebase-adminsdk-je0pw-1b6a0a95b6.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://microbit-75378-default-rtdb.europe-west1.firebasedatabase.app/'})

ref = db.reference()

ref = db.reference().child('transistor')
ref.listen(doSomething)
ref.update ({str(time.time()):'random'})