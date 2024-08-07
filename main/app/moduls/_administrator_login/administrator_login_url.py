from django.urls import path

from . import administrator_login_view

urlpatterns = [
    path('url/', administrator_login_view),
]
