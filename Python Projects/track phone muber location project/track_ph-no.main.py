import phonenumbers    #pip install phonenumbers
from test import number
from phonenumbers import geocoder #geocoder is a built in function
phone_number = phonenumbers.parse(number,"CH")  #CH means country history
print(geocoder.description_for_number(phone_number,"en")) #en means english

from phonenumbers import carrier
service_name = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_name,"en"))
