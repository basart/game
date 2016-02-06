from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm, PasswordInput


class LogGameEvents(models.Model):
    id = models.BigIntegerField(primary_key=True)
    player = models.ForeignKey('Players')
    event_type = models.IntegerField()
    event_data = models.TextField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'log_game_events'


class PlayerAchievements(models.Model):
    player = models.ForeignKey('Players')
    achievement_id = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_achievements'
        #unique_together = (('player_id', 'achievement_id'),)


class PlayerSessions(models.Model):
    player = models.ForeignKey('Players')
    sid = models.CharField(unique=True, max_length=40)
    ip_addr = models.CharField(max_length=25, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'player_sessions'


class PlayerStats(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey('Players')
    stat_id = models.IntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_stats'


class Players(models.Model):
    nickname = models.CharField(unique=True, max_length=50)
    xp = models.IntegerField()
    email = models.EmailField(unique=True, max_length=200)
    password_hash = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'players'

    def __unicode__(self):
        return self.nickname


class PlayersForm(ModelForm):
    class Meta:
        model = Players
        fields = ['nickname', 'email', 'password_hash']
