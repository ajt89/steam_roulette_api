import requests
from random import randrange

from .models import SteamApp


STEAM_API_HOSTNAME = 'https://api.steampowered.com/'
STEAM_APPS_URI = 'ISteamApps/'
STEAM_APP_LIST_URI = 'GetAppList/v2/'

STORE_API_HOSTNAME = 'http://store.steampowered.com/'
STORE_API_URI = 'api/'
STORE_APP_DETAILS_URI = 'appdetails/'
STORE_APP_ID_URI = '?appids='


def get_games():
    hostname = STEAM_API_HOSTNAME + STEAM_APPS_URI + STEAM_APP_LIST_URI
    response = requests.get(hostname)
    apps_json = response.json()
    app_list = apps_json['applist']['apps']

    for app in app_list:
        SteamApp.objects.create(appid=app['appid'], name=app['name'])


def choose_game():
    """ Gets alls games and randomly chooses one """
    sa = SteamApp.objects.all().only('name')
    max_count = sa.count()

    chosen_game_dict = sa[randrange(0, max_count, 2)]
    return chosen_game_dict


def retrieve_game_details(appid):
    """ Gets details for a given game """
    hostname = STORE_API_HOSTNAME + STORE_API_URI + STORE_APP_DETAILS_URI + STORE_APP_ID_URI + str(appid)
    print hostname
    response = requests.get(hostname)
    game_detial_json = response.json()
    game_details = response.content
    return game_details
