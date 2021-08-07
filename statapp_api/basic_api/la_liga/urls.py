from django.urls import include, path
from .views import laLigaTeamsCreate, laLigaTeamsList, laLigaTeamsDetail, laLigaTeamsUpdate, laLigaTeamsDelete


urlpatterns = [
    path('create/', laLigaTeamsCreate.as_view(), name='create-laLigaTeams'),
    path('', laLigaTeamsList.as_view()),
    path('<int:pk>/', laLigaTeamsDetail.as_view(), name='retrieve-laLigaTeams'),
    path('update/<int:pk>/', laLigaTeamsUpdate.as_view(), name='update-laLigaTeams'),
    path('delete/<int:pk>/', laLigaTeamsDelete.as_view(), name='delete-laLigaTeams')
]