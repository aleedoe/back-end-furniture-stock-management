from django.urls import path

from . import user_view

urlpatterns = [
    path('url/', user_view),
]
