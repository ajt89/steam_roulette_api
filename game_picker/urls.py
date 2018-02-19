from django.conf.urls import url

from game_picker import views

urlpatterns = [
    url(r'all/?$', views.all),
]

api_urls = (
    '/game_picker/all',
)
