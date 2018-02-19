# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests

from django.http import HttpResponse

from game_picker_api import get_games, choose_game


def all(request):
    game = choose_game()
    return HttpResponse(game)
