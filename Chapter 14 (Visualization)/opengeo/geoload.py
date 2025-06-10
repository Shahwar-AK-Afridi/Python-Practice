#This code spiders the GeoApi.

import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

# https://py4e-data.dr-chuck.net/opengeo?q=Ann+Arbor%2C+MI
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?' #proxy of GeoAPI is created so that we have to create account on "Geoapify"
#Proxy doesnot require a key, however it has a rate-limit.(Just for the class) for real time programs we have to create account on "Geoapify"
# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''') #Key= address & Value= geodata (JSON) 

# Ignore SSL certificate errors, as many certificates are not included in python. It just make sure the "URLlib" works.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("A:/Coursera/Python/py4e/Python-Practice/Chapter 14 (Visualization)/opengeo/where.data")
count = 0
nofound = 0
for line in fh:
    if count > 100 :  #if we have retrieved 100 locations then we stop as it is restartable process
        print('Retrieved 100 locations, restart to retrieve more')
        break

    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))  #We are checking the whether address is already been retrieved from API or not

    try:
        data = cur.fetchone()[0]
        print("Found in database", address) #If address already exist in DB, we move on to next iteration.
        continue
    except:
        pass
    
    #If the address doesnot exist in DB then follow below code.
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)  #Here are creating URL of each location
    # "urllib.parse.urlencode(parms)" because we have to encode the string Eg: Ann Arbor MI --> Ann+Arbor%2C+MI

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx) #Used to ignore SSL Certificate errors

    data = uh.read().decode() #converting UTF-8 JSON TO Unicode JSON.

    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' ')) #Debugging Statement
    count = count + 1

    try:
        js = json.loads(data)  #JSON to disctiony/list conversion
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if not js or 'features' not in js:    #Sanity Check to confirm we got real data
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:         #Sanity Check to confirm we got real data
        print('==== Object not found ====')
        nofound = nofound + 1

    cur.execute('''INSERT INTO Locations (address, geodata)   
        VALUES ( ?, ? )''',
        (memoryview(address.encode()), memoryview(data.encode()) ) ) #Insert into DB.

    conn.commit()

    if count % 10 == 0 :       #Pause for few seconds.
        print('Pausing for a bit...')
        time.sleep(5)

if nofound > 0:
    print('Number of features for which the location could not be found:', nofound)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")

