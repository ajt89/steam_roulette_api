# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests

from django.http import HttpResponse

from game_picker_api import get_games, choose_game, retrieve_game_details


def all(request):
    game_obj = choose_game()
    game_details = retrieve_game_details(game_obj.appid)
    return HttpResponse(game_details)
