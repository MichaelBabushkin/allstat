from rest_framework import serializers
from .models import premierLeagueTeams

class premierLeagueTeamsSerializer(serializers.ModelSerializer):

    class Meta:
        model = premierLeagueTeams 
        fields = ['pk', 'name', 'country', 'shortCode','logo']