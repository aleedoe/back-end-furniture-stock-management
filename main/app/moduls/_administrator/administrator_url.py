from django.urls import path

from . import administrator_view

urlpatterns = [
    path('administrator/', administrator_view.administratorList),
    path('administrator/<int:id>/', administrator_view.administrator),
]
