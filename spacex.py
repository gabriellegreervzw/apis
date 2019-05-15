#! /usr/bin/python3

import requests
import webbrowser
import pprint


url = 'https://api.spacexdata.com/v3/launches/latest'

data = requests.get(url)
json_data = data.json()
pprint.pprint(json_data)

print("The Mission Name is: ", json_data['mission_name'])
print("The launch data is: ", json_data['launch_date_local'])
print("The flight number is: ", json_data['flight_number'])

#print("Links to choose from: ", json_data['links']['flickr_images'])

link_list = json_data['links']['flickr_images']

mission_patch_jpg = json_data['links']['mission_patch']

input("PRESS ENTER TO ACCESS.....")
webbrowser.open(mission_patch_jpg)

