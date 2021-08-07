from django.urls import include, path
from .views import premierLeagueTeamsCreate, premierLeagueTeamsList, premierLeagueTeamsDetail, premierLeagueTeamsUpdate, premierLeagueTeamsDelete


urlpatterns = [
    path('create/', premierLeagueTeamsCreate.as_view(), name='create-premierLeagueTeams'),
    path('', premierLeagueTeamsList.as_view()),
    path('<int:pk>/', premierLeagueTeamsDetail.as_view(), name='retrieve-premierLeagueTeams'),
    path('update/<int:pk>/', premierLeagueTeamsUpdate.as_view(), name='update-premierLeagueTeams'),
    path('delete/<int:pk>/', premierLeagueTeamsDelete.as_view(), name='delete-premierLeagueTeams'),
]