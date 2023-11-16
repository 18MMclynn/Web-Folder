import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/Users/18MMcLynn.ACC/Desktop/Python/fir-1-eb8ba-firebase-adminsdk-vl3ez-89e6f3196b.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://fir-1-eb8ba-default-rtdb.europe-west1.firebasedatabase.app/'})

ref = db.reference().child('classes')

results = ref.get()
#print(results)
#print(type(results))
for k,v in results.items():
    print("Key is: ", k,"\t value is: ",v)
    for k2, v2 in v.items():
        print("Key is: ",k2, "\t value is: ",v2)