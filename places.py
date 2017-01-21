from flask import Flask
#import googlemaps
import requests
import json

#gmaps = googlemaps.Client(key='AIzaSyAer4VW66byYQj08TzM2LYzWcRy2xcy_B8')

#search = places(gmaps, "animal control near me", location=)

send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
lat = j['latitude']
lon = j['longitude']

r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query=animal+control+in+my+area&location='+str(lat)+','+str(lon)+'&key=AIzaSyAer4VW66byYQj08TzM2LYzWcRy2xcy_B8')
j = json.loads(r.text)

result = []


for ref in j['results']:
    result.append(ref['place_id'])
    if len(result) == 1:
        break

for id in result:
    r = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='+id+'&key=AIzaSyAer4VW66byYQj08TzM2LYzWcRy2xcy_B8')
    j = json.loads(r.text)

phone = j['result']

app = Flask(__name__)

@app.route('/')
def hello_world():
    return str(phone['international_phone_number'])
