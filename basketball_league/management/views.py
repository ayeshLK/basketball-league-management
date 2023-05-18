from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from management.models import Coach, Team, Player, Game
from management.serializers import CoachSerializer, TeamSerializer, PlayerSerializer

class CoachViewSet(viewsets.ModelViewSet):
    """
    This view set provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions for Coach model.
    """
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

class TeamViewSet(viewsets.ModelViewSet):
    """
    This view set provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions for Team model.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    """
    This view set provides 'list', 'create' actions for Players in a team.
    """
    serializer_class = PlayerSerializer

    def get_queryset(self):
        return Player.objects.filter(team=self.kwargs['team_pk'])

    def perform_create(self, serializer):
        team = Team.objects.get(pk=self.kwargs['team_pk'])
        serializer.save(team=team)
    
