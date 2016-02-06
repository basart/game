from django.contrib import admin
from .models import PlayerAchievements, Players, PlayerSessions, PlayerStats, LogGameEvents
# Register your models here.


@admin.register(PlayerAchievements, Players, PlayerSessions, PlayerStats, LogGameEvents)
class PersonAdmin(admin.ModelAdmin):
    pass



