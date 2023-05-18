from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from management.views import CoachViewSet, TeamViewSet, PlayerViewSet

router = DefaultRouter()
router.register(r'coaches', CoachViewSet, basename="coach")
router.register(r'teams', TeamViewSet, basename="team")
nested_teams_router = routers.NestedSimpleRouter(router, r'teams', lookup='team')
nested_teams_router.register(r'players', PlayerViewSet, basename='player')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(nested_teams_router.urls)),
]
