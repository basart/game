from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('players.urls')),
    url(r'^auth/', include('loginsys.urls'))
]
