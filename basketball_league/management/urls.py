from django.urls import path, include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views
from management.views import hello_world

urlpatterns = [
    path('hello-world', hello_world)
]

urlpatterns = format_suffix_patterns(urlpatterns)
