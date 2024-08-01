from django.urls import path

from . import furniture_view

urlpatterns = [
    path('url/', furniture_view),
]
