import pyrebase
import numpy as np
config = {
  "apiKey": "AIzaSyDwDvkOBpnLY7GB22axtQc2xnLnJgQAVyU",
  "authDomain": "parking-233cc.firebaseapp.com",
  "databaseURL": "https://parking-233cc.firebaseio.com",
  "storageBucket": "parking-233cc.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
ind = 0
status = False
while ind < 16:
	location = "parking1/space-" + str(ind)
	data = {
		location: status}
	db.update(data)
	ind += 1