#!/usr/bin/python

import requests
import json
import urllib2
from light import Light
import ConfigParser
import datetime

config = ConfigParser.RawConfigParser()
config.read('hue.cfg')
ip = config.get('hue', 'ip')
secret = config.get('hue', 'secret')

light = Light(ip, secret, 4)

portland = 5746545
GMTOffset = -8
url = 'http://openweathermap.org/data/2.1/forecast/city/%s' % portland
r = requests.get(url)
data = json.loads(r.content)

weather = []
for cast in data['list']:
    u = datetime.date.fromtimestamp(cast['dt'] - 60*60*GMTOffset)
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    if(u < tomorrow):
        weather.append(cast['weather'][0]['main'])

if('Rain' in weather):
    print "Set light blue for rain"
    light.on()
    light.blue()
elif('Clear' in weather):
    print "Set light green for clear"
    light.on()
    light.green()
