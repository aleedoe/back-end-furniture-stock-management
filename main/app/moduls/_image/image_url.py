from django.urls import path

from . import image_view

urlpatterns = [
    path('url/', image_view),
]
