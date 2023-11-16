import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = creedentials.Certificate(""
firebase_admin.initialize_app(cred,{'databaseURL':

ref = db.reference().child('classes').child('Biology123')
ref.update.({'Description':'Biology123 class', 'id':'Biology','title':'Biology123'})
ref = db.reference().child('classes').child('Math123')
ref.update({'Description':'Math123','id':'Math123','title':'Math 123'})