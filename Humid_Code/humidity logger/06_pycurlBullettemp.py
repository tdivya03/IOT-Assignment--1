#!/usr/bin/env python3
import requests
import json
import os
import sensehat

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

#main function
def main():
    ip_address = os.popen('hostname -I').read()
	temp = sense.get_temperature()
	
    send_notification_via_pushbullet(ip_address,temp, "From Raspberry Pi")

#Execute
main()
