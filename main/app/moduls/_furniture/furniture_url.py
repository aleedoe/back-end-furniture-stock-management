from django.urls import path

from . import furniture_view

urlpatterns = [
    path('category/', furniture_view.categoryList),
    path('furniture/', furniture_view.furnitureList),
]
