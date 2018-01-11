#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyowm
import tweepy, time, sys#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:

CONSUMER_KEY = 'd7ovEgieUXHSGDrAEjTMmBf4a'  # Enter consumer key
CONSUMER_SECRET = 'IQaXjSZJbDAtYyV4unqocK5zNNFKlOOpxkp07Cn8kYicZaZ3JH'  # Enter consumer secret key
ACCESS_KEY = '878694779797852160-4SUCLzE2KBgpGCxpBLUyCMDsku0kETu'  # Enter access token
ACCESS_SECRET = 'HlCDsVvV74VwyeUeFGnaIrEDh2EPGCHP9pOmHhhzVw26D'  # Enter access token secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()


for line in f:
    for status in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(status.id)
        except:
            pass


    api.update_status(status = line)
    time.sleep(15)  # Tweet every 15 Pyth  minutes

#argfile = str(sys.argv[1])

# enter the corresponding information from your Twitter application:

CONSUMER_KEY = '6T10WDz0WVLMcfbe4NtALhHHG'  # Enter consumer key
CONSUMER_SECRET = '68y1bi6jQ7Z4IcrcxCEQRGYRVm6kCNiJW0YyslsfI9cC9G7Few'  # Enter consumer secret key
ACCESS_KEY = ' 75185557-XsvDVdOpY2WuZkYSxqHzdrqvfTZ0wvbTOJgucOJOP'  # Enter access token
ACCESS_SECRET = ' XeOA8syjVT7x2fMfGJAiyrlOH66a53D9JMfkKq7OgdQ6p'  # Enter access token secret


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)


owm = pyowm.OWM('05b31851d9b125b2e434df47defa5541')
while (1):
    observation = owm.weather_at_place("Halmstad,sweden")
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')
    tomorrow = pyowm.timeutils.tomorrow()
    wind = w.get_wind()
    for status in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(status.id)
        except:
            pass
    api.update_status(wind)
    time.sleep(20)