#!/usr/bin/env python3
import os
from datetime import datetime
from flask import Flask, render_template, request
from sense_hat import SenseHat
import sqlite3 as lite
app = Flask(__name__)

'''Uncomment if you dont want to see console print out'''
#import logging
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)
con = lite.connect('sensehat.db')

#get time and temp data from sense hat raspberry
def getData():
    time = datetime.now().strftime("%H:%M:%S")
    sense = SenseHat()
    temp = round(sense.get_temperature(), 1)
    return time, temp

#approach to get data from sensehat database
def getDatafromDB():
    with con:
          cur = con.cursor()
          data=cur.execute("Select * from SENSEHAT_data")
          for row in cur.execute('SELECT * FROM SENSEHAT_data'):
                 return row

# main route 
@app.route("/")
def index():	
	time, temp = getData()
	templateData = {
		'time': time,
		'temp': temp
	}
	return render_template('index.html', **templateData)

if __name__ == "__main__":
	host = os.popen('hostname -I').read()
	app.run(host=host, port=80, debug=False)
