"""
URL configuration for spotify_apps project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('spotify_map.urls')),
]
