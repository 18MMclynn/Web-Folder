import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = creedentials.Certificate(""
firebase_admin.initialize_app(cred,{'databaseURL':

ref = db.reference().child('classes').child('Biology123')