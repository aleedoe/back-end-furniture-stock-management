from django.urls import path

from . import warehouser_view

urlpatterns = [
    path('warehouser/', warehouser_view.warehouserList),
]
