from django.urls import path

from . import reseller_login_view

urlpatterns = [
    path('url/', reseller_login_view),
]
