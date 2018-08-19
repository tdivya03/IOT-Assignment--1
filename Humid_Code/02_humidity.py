from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

humid = sense.get_humidity()
sense.show_message('humid:{0:0.1f}%'.format(humid),scroll_speed=0.05)
sense.clear()
