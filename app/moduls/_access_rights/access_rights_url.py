from django.urls import path

from . import access_rights_view

urlpatterns = [
    path('url/', access_rights_view),
]
