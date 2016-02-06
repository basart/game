from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^players/$', views.show_players),
    url(r'^players/page/(\d+)/$', views.show_players),
    url(r'^players/player/([0-9]+)/$', views.show_player_form),
    url(r'^players/search/?$', views.search_player),
    url(r'^player/change_xp/([0-9]+)/$', views.change_xp),
]
