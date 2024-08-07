from django.urls import path

from . import reseller_signin_view

urlpatterns = [
    path('url/', reseller_signin_view),
]
