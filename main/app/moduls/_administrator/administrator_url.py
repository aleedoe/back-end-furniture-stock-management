from django.urls import path

from . import administrator_view

urlpatterns = [
    path('administrator/', administrator_view.administratorList),
]
