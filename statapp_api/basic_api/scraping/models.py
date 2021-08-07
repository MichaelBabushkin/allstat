from django.db import models
from django.utils import timezone 

class teamPlayers(models.Model):
    team = models.CharField("team", max_length=24)
    player_id = models.CharField("player_id", max_length=24)
    player_name = models.CharField("player_name", max_length=50)
    games = models.CharField("games", max_length=10)
    time = models.CharField("time", max_length=10)
    goals = models.CharField("goals", max_length=10)
    xG = models.CharField("xG", max_length=50)
    assists = models.CharField("assists", max_length=50)
    xA = models.CharField("xA", max_length=50)
    shots = models.CharField("shots", max_length=50)
    key_passes = models.CharField("key_passes", max_length=50)
    yellow_cards = models.CharField("yellow_cards", max_length=10)
    red_cards = models.CharField("red_cards", max_length=10)
    position = models.CharField("position", max_length=10)
    team_title = models.CharField("team_title", max_length=50)
    npg = models.CharField("npg", max_length=10)
    npxG = models.CharField("npxG", max_length=50)
    xGChain = models.CharField("xGChain", max_length=50)
    xGBuildup = models.CharField("xGBuildup", max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.team