from django.urls import path

from . import administrator_view

urlpatterns = [
    path('url/', administrator_view),
]
