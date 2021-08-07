from django.shortcuts import render
from .models import laLigaTeams
from rest_framework import generics
from .serializers import laLigaTeamsSerializer


class laLigaTeamsCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new laLigaTeams
    queryset = laLigaTeams.objects.all(),
    serializer_class = laLigaTeamsSerializer


class laLigaTeamsList(generics.ListAPIView):
    # API endpoint that allows laLigaTeams to be viewed.
    queryset = laLigaTeams.objects.all()
    serializer_class = laLigaTeamsSerializer

class laLigaTeamsDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single laLigaTeams by pk.
    queryset = laLigaTeams.objects.all()
    serializer_class = laLigaTeamsSerializer

class laLigaTeamsUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a laLigaTeams record to be updated.
    queryset = laLigaTeams.objects.all()
    serializer_class = laLigaTeamsSerializer

class laLigaTeamsDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a laLigaTeams record to be deleted.
    queryset = laLigaTeams.objects.all()
    serializer_class = laLigaTeamsSerializer
