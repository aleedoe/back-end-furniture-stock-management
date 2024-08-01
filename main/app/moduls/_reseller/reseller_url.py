from django.urls import path

from . import reseller_view

urlpatterns = [
    path('url/', reseller_view),
]
