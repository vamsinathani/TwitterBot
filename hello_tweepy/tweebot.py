import tweepy, time, sys
import pyowm


# enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'd7ovEgieUXHSGDrAEjTMmBf4a'  # Enter consumer key
CONSUMER_SECRET = 'IQaXjSZJbDAtYyV4unqocK5zNNFKlOOpxkp07Cn8kYicZaZ3JH'  # Enter consumer secret key
ACCESS_KEY = '878694779797852160-4SUCLzE2KBgpGCxpBLUyCMDsku0kETu'  # Enter access token
ACCESS_SECRET = 'HlCDsVvV74VwyeUeFGnaIrEDh2EPGCHP9pOmHhhzVw26D'  # Enter access token secrets token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

owm = pyowm.OWM('8436a80488c88fa30837482ea3841891')
observation = owm.weather_at_place("Halmstad,sweden")
w = observation.get_weather()
print (w.get_status())

line = 'Hello everyone ! current Weather status in Halmstad Sweden is ' + w.get_status()

for status in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(status.id)
        except:
            pass
api.update_status(line)