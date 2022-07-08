import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
import time
import requests 
api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
            
import json
location_req_url='http://api.ipstack.com/103.51.95.183?access_key=0749695b4d979242e57c4fe66ccc71e7'
r = requests.get(location_req_url)
location_obj = json.loads(r.text)
        
lat = location_obj['latitude']
lon = location_obj['longitude']
latitude = lat
longitude = lon
print(str(latitude))
print(str(longitude))
msg ="I am in trouble..need Help!!!Here I attached mylocation:Latitude is:"+str(latitude)+"Langitude is:"+str(longitude)
def sms_send():
    url="https://www.fast2sms.com/dev/bulkV2"
    params={
  
        "authorization":"Y9i3Je0fkBLVHPtSZv1NJJHdlONt1Vr2aRObSXVHhkl0AgC6nLLp4YuCPbk2",
        "sender_id":"FTWSMS",
        "message":msg,
        "language":"english",
        "route":"p",
        "numbers":"8669729811"
    }
    rs=requests.get(url,params=params)
    
while True: # Run forever
    button = GPIO.input(16)
    print (button)
    if (button == 1):
        print("Button was pushed!")
        time.sleep(0.3)
        sms_send()
    elif (button == 0):
        print("Button was Up!")  
        time.sleep(0.3)
        sms_send()
   

