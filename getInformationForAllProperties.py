from functions import *
import json

token = json.loads(login("email", "password"))['accessToken']
#Hi dude this login is not happening
Markdown here!

Hi I am trying to connect to upalnd api using the same code

getting error
"HTTPError: 403 Client Error: Forbidden for url: https://api.upland.me/authentication
Do you know ,if the api access is still allowed ?
"

IDList = open("idsToProcess.txt", "w+")

raw = getNearbyPropertiesClusters(token, 37.815619195130225, 37.56300036761387, -122.34690909477374, -122.53147845840631)
JSON = json.loads(raw)

for Property in JSON['clusters']:
    prop_id = Property['prop_id']
    IDList.write(str(prop_id))
    IDList.write("\n")
IDList.close()

with open('idsToProcess.txt') as f:
    lines = [line.rstrip() for line in f]

for line in lines:
    try:
        info = json.loads(getPropertyInformation(token, line))
        full_address = info['full_address']
        centerlat = info['centerlat']
        centerlng = info['centerlng']
        area = info['area']
        status = info['status']
        last_purchased_price = info['last_purchased_price']
        is_offering = info['is_offering']
        is_blocked = info['is_blocked']
        owner = info['owner']
        owner_username = info['owner_username']
        yield_per_hour = info['yield_per_hour']
        price = info['price']
        country = info['country']
        city = info['city']
        teleport_price = info['teleport_price']
        print(str(line) + ","
            + full_address + ","
            + str(centerlat) + ","
            + str(centerlng) + ","
            + str(area) + ","
            + status + ","
            + str(last_purchased_price) + ","
            + str(is_offering) + ","
            + str(is_blocked) + ","
            + owner + ","
            + owner_username + ","
            + str(yield_per_hour) + ","
            + str(price) + ","
            + country + ","
            + city + ","
            + str(teleport_price))
    except:
        pass
