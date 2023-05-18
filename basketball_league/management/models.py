from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPES = (
    ('admin', 'Admin'),
    ('coach', 'Coach'),
    ('player', 'Player')
)

class User(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

class SiteUsage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="site_usages")
    login = models.DateTimeField()
    logout = models.DateTimeField(blank=True)
    duration = models.DurationField()

class Coach(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        ordering = ['name']

class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.OneToOneField(Coach, on_delete=models.CASCADE)
    class Meta:
        ordering = ['name']

class Player(models.Model):
    name = models.CharField(max_length=100)
    height = models.PositiveBigIntegerField()
    average_score = models.DecimalField(max_digits=5, decimal_places=2)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")
    class Meta:
        ordering = ['name']

class Game(models.Model):
    venue = models.CharField(max_length=100)
    date = models.DateField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_games")
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_games")

class TeamGame(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()

class Participation(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="participations")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="participations")

