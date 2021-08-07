from django.shortcuts import render
from .models import premierLeagueTeams
from rest_framework import generics
from .serializers import premierLeagueTeamsSerializer

class premierLeagueTeamsCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new premierLeagueTeams
    queryset = premierLeagueTeams.objects.all(),
    serializer_class = premierLeagueTeamsSerializer


class premierLeagueTeamsList(generics.ListAPIView):
    # API endpoint that allows premierLeagueTeams to be viewed.
    queryset = premierLeagueTeams.objects.all()
    serializer_class = premierLeagueTeamsSerializer

class premierLeagueTeamsDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single premierLeagueTeams by pk.
    queryset = premierLeagueTeams.objects.all()
    serializer_class = premierLeagueTeamsSerializer

class premierLeagueTeamsUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a premierLeagueTeams record to be updated.
    queryset = premierLeagueTeams.objects.all()
    serializer_class = premierLeagueTeamsSerializer

class premierLeagueTeamsDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a premierLeagueTeams record to be deleted.
    queryset = premierLeagueTeams.objects.all()
    serializer_class = premierLeagueTeamsSerializer

