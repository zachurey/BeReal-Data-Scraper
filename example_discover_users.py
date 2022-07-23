"""
    Example file for how to use the BeReal API wrapper to discover users
"""

from json import dumps
from random import randint
from time import sleep

from BeReal.bereal_access_token import BeRealAccessToken
from BeReal.bereal_discover_users import BeRealDiscoverUsers

access_token = BeRealAccessToken().get_access_token()
discover_users = BeRealDiscoverUsers(access_token=access_token)

all_objects = []

for x in range(5):
    json_response = discover_users.get_discover_users_json()

    for element in json_response['posts']:
        new_object = { 'profilePicture': '', 'post': {} }
        front_picture_url = element['photoURL']
        rear_picture_url = element['secondaryPhotoURL']

        new_object['post']['frontPictureURL'] = front_picture_url
        new_object['post']['rearPictureURL'] = rear_picture_url

        if 'profilePicture' in element['user']:
            profile_picture = element['user']['profilePicture']['url']
            new_object['profilepicture'] = profile_picture

        all_objects.append(new_object)

    sleep(randint(1, 3))

output = open('data.json', 'w', encoding='utf-8')
output.write(dumps(all_objects))
output.close()
