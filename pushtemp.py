#!/usr/bin/env python3
import requests
import json
import os
from sense_hat import SenseHat

ACCESS_TOKEN="o.X75S09HiwhN9Z4NMaDzyl0Is0vrawu9c"

def send_notification_via_pushbullet(title, body):
    """ Sending notification via pushbullet.
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    """
    data_send = {"type": "note", "title": title, "body": body}
 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 
                         'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')
# defining temperatue notification
#main function
def main ():
    sense = SenseHat ()
    temp = sense.get_temperature ()
    temp = round(temp,1)
    if temp < 20.0:
       ip_address = os.popen('hostname -I').read()
       send_notification_via_pushbullet(ip_address,"Temperature is cool,wear a jacket")     
    else:
       send_notification_via_pushbullet(ip_address,"Temperature is pleasant and no need for a jacket")

#Execute
main()
