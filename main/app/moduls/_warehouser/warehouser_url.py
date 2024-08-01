from django.urls import path

from . import warehouser_view

urlpatterns = [
    path('url/', warehouser_view),
]
