from firebase import firebase
import time
myDBConn = firebase.FirebaseApplication('https://test-firebase-2d7c9-default-rtdb.europe-west1.firebasedatabase.app/',None)

data = {
    "ID": 1234567890,
    "name":"Bob",
    "age":21005
    }

myDBConn.patch('/User1/'+str(int(time.time() * 1000)),data)

result = myDBConn.get('/User1/',None)
print(result)
for key in result:
    print(type(result[key]))
    for k,v in result[key].items():
        print(k +" -- "+str(v))
    print(key)