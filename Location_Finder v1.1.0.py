'''
©Data Random
'''

#importing_Libs
#---------------------------------#

import phonenumbers
import folium 
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

#Asking_for_Phone_Number
#---------------------------------#
number = input("Enter your phone Number : ")

#Getting_API_key
#---------------------------------#
key = 'Put your opemcage Api Key'


#Getting_The_Country
#---------------------------------#
get_number = phonenumbers.parse(number)
location = geocoder.description_for_number(get_number , "en")
print(location)


#Getting_The_Service_provider_details
#---------------------------------#
provider = phonenumbers.parse(number)
print(carrier.name_for_number(provider, "en"))


#Getting_The_Actual_location(Not Accurate)
#---------------------------------#
geocoder= OpenCageGeocode(key)
asked = str(location)     
result = geocoder.geocode(asked)

#Filtering_the_Data
#---------------------------------#
lat = result[0]['geometry']['lat']
long = result[0]['geometry']['lng']

#Printing_the_latitudnal_and_longitudnal_locaton(Not Accurate)
#---------------------------------#
print(lat,long)


#Making_A_Map(.html)
#---------------------------------#
map_my = folium.Map(location=[lat , long ] , zoom_start= 9 )
folium.Marker([lat , long ], popup = location).add_to((map_my))


#Saving_the_map(.html)
#---------------------------------#
map_my.save("Map.html")
