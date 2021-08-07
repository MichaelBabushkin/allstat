from rest_framework import serializers
from .models import laLigaTeams

class laLigaTeamsSerializer(serializers.ModelSerializer):

    class Meta:
        model = laLigaTeams 
        fields = ['pk', 'name', 'country', 'shortCode','logo']