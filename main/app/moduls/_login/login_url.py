from django.urls import path

from . import login_view

urlpatterns = [
    path('url/', login_view),
]
