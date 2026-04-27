from django.urls import path

from team_players import views

#This is for  Seialization
urlpatterns = [
    path('api/v1/players/',views.player_list),
    path('api/v1/snippet/<int:id>/',views.player_about),
]


#This os for De-Seialization
urlpatterns = [
    path('api/v1/players/',views.players_list),
    path('api/v1/snippet/<int:id>/',views.players_about),
    
]

