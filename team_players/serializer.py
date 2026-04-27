from rest_framework import serializers

from team_players.models import Player_Details

from team_players import models

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Player_Details
        fields='__all__'