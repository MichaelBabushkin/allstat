from rest_framework import serializers
from .models import teamPlayers

class scrapingSerializer(serializers.ModelSerializer):

    class Meta:
        model = teamPlayers 
        fields = ['player_id', 'player_name', 'games', 'time','goals']