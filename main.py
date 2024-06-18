import phonenumbers
import os
import folium
from dotenv import load_dotenv
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

load_dotenv()

number = os.getenv('NUMBER')
key = os.getenv("GEOCODEAPI")

parsed_number = phonenumbers.parse(number)
location = geocoder.description_for_number(parsed_number, 'en')

carrier_name = carrier.name_for_number(parsed_number, "en")

geocoder_info = OpenCageGeocode(key)
query = str(location)
result = geocoder_info.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']


myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("myLocation.html") #file name in which your location will be saved

print(location)
print(carrier_name)
# print(result)
print(lat, lng)