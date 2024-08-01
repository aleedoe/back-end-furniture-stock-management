from django.urls import path

from . import transaction_view

urlpatterns = [
    path('url/', transaction_view),
]
