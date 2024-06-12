import phonenumbers
import os
from dotenv import load_dotenv
from phonenumbers import geocoder, carrier

load_dotenv()

number = os.getenv('NUMBER')
parsed_number = phonenumbers.parse(number)
location = geocoder.description_for_number(parsed_number, 'en')

carrier_name = carrier.name_for_number(parsed_number, "en")

print(location)
print(carrier_name)

