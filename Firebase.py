import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = creedentials.Certificate("C:/Users/18MMcLynn.ACC/Desktop/Python/fir-1-eb8ba-firebase-adminsdk-vl3ez-89e6f3196b.json")

firebase_admin.initialize_app(cred,{'databaseURL': 'https://fir-1-eb8ba-default-rtdb.europe-west1.firebasedatabase.app/'})

ref = db.reference().child('classes').child('Biology123')
ref.update.({'Description':'Biology123 class', 'id':'Biology','title':'Biology123'})
ref = db.reference().child('classes').child('Math123')
ref.update({'Description':'Math123','id':'Math123','title':'Math 123'})