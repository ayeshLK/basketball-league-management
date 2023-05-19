from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedIdentityField
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer
from management.models import Game, Team, Coach, Player

class GameSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'date', 'venue', 'home_team', 'away_team']

class CoachSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Coach
        fields = ['url', 'id', 'name']


class TeamSerializer(HyperlinkedModelSerializer):
    players = HyperlinkedIdentityField(view_name='player-list', lookup_url_kwarg='team_pk')
    players_avg_over_90 = HyperlinkedIdentityField(view_name="team-percentile90")
    class Meta:
        model = Team
        fields = ['url', 'id', 'name', 'coach', 'players', 'players_avg_over_90']

class PlayerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'height', 'average_score']

