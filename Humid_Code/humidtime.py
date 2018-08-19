#!/usr/bin/env python3
# more info: https://pypi.org/project/python-crontab/
import time
import os   
from sense_hat import SenseHat


os.environ['TZ'] = 'Australia/Melbourne'
time.tzset()
sense = SenseHat()
sense.show_message('Time is NoW {}'.format(time.strftime('%X')), scroll_speed=0.05)

