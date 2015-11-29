__author__ = 'kwoshvick'

import urllib
import urllib.parse as parse
import urllib.request as rq
import json
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input("Enter Location : ")
    if len(address) < 1: break

    url = serviceurl+parse.urlencode({'sensor':'false','address':address})
    print('Retrieving',url)
    uh = rq.urlopen(url)
    data = uh.read()
    print('Retrieved ', len(data), ' characters')

    try:
        js = json.loads(data.decode())
    except:js = None
    if 'status' not in js or js["status"] != 'OK':
        print('======= FAILURE TO RETRIEVE ===========')
        print(data)
        continue
    print(json.dumps(js,indent=4))
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat:',lat,' lng:',lng)
    location = js['results'][0]['formatted_address']
    print(location)

