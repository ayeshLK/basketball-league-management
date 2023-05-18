from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedIdentityField
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer
from management.models import Team, Coach, Player

class CoachSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Coach
        fields = ['url', 'id', 'name']


class TeamSerializer(HyperlinkedModelSerializer):
    players = HyperlinkedIdentityField(view_name='player-list', lookup_url_kwarg='team_pk')
    class Meta:
        model = Team
        fields = ['url', 'id', 'name', 'coach', 'players']

class PlayerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'height', 'average_score']