from django.shortcuts import render
from .models import premierLeagueTeams
from rest_framework import generics
from .serializers import premierLeagueTeamsSerializer
# import json
# import pandas as pd
# import requests

# from django.core.management.base import BaseCommand
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import json

# class Command(BaseCommand):
#     help = "collect jobs"
#     # define logic of command
#     def handle(self, *args, **options):
#         # collect html
#         html = urlopen('https://jobs.lever.co/opencare')
#         # convert to soup
#         soup = BeautifulSoup(html, 'html.parser')
#         # grab all postings
#         postings = soup.find_all("div", class_="posting")
#         for p in postings:
#             url = p.find('a', class_='posting-btn-submit')['href']
#             title = p.find('h5').text
#             location = p.find('span', class_='sort-by-location').text
#             # check if url in db
#             try:
#                 # save in db
#                 Job.objects.create(
#                     url=url,
#                     title=title,
#                     location=location
#                 )
#                 print('%s added' % (title,))
#             except:
#                 print('%s already exists' % (title,))
#         self.stdout.write( 'job complete' )

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

