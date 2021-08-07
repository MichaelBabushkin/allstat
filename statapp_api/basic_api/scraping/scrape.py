from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import requests
from .models import teamPlayers

class Command(BaseCommand):
# define logic of command
    def handle(self, *args, **options):
        # collect html
        html = 'https://understat.com/team/Manchester_United/2020'
        # convert to soup
        res = requests.get(html)
        soup = BeautifulSoup(res.content, 'html.parser')
        scripts = soup.find_all('script')
        strings = scripts[3].string     
        ind_start = strings.index("('")+2
        ind_end = strings.index("')")
        json_data = strings[ind_start:ind_end]
        json_data = json_data.encode('utf8').decode('unicode_escape')
        obj = json.loads(json_data)
        # Using for loop
        players = []
        for i in obj:
            players.append(i['player_name']) 
            print(i) 
    #     player_stats= teamPlayers()   player_id = models.CharField("player_id", max_length=24)
    # player_name = models.CharField("player_name", max_length=50)
    # games = models.CharField("games", max_length=10)
    # time = models.CharField("time", max_length=10)
    # goals = models.CharField("goals", max_length=10)
    # xG = models.CharField("xG", max_length=50)
    # assists = models.CharField("assists", max_length=50)
    # xA = models.CharField("xA", max_length=50)
    # shots = models.CharField("shots", max_length=50)
    # key_passes = models.CharField("key_passes", max_length=50)
    # yellow_cards = models.CharField("yellow_cards", max_length=10)
    # red_cards = models.CharField("red_cards", max_length=10)
    # position = models.CharField("position", max_length=10)
    # team_title = models.CharField("team_title", max_length=50)
    # npg = models.CharField("npg", max_length=10)
    # npxG = models.CharField("npxG", max_length=50)
    # xGChain = models.CharField("xGChain", max_length=50)
    # xGBuildup = models.CharField("xGBuildup", max_length=50)
    # created_date = models.DateTimeField(default=timezone.now)



fetched = Command()
fetched.handle()