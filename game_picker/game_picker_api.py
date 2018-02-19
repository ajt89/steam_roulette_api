import requests
from random import randrange

from .models import SteamApp


STEAM_API_HOSTNAME = 'https://api.steampowered.com/'
STEAM_APPS_URI = 'ISteamApps/'
STEAM_APP_LIST_URI = 'GetAppList/v2/'


def get_games():
    hostname = STEAM_API_HOSTNAME + STEAM_APPS_URI + STEAM_APP_LIST_URI
    response = requests.get(hostname)
    apps_json = response.json()
    app_list = apps_json['applist']['apps']

    for app in app_list:
        SteamApp.objects.create(appid=app['appid'], name=app['name'])


def choose_game():
    sa = SteamApp.objects.all().only('name')
    max_count = sa.count()

    chosen_game = sa[randrange(0, max_count, 2)]
    return chosen_game.name
