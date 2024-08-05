from django.urls import path

from . import reseller_view

urlpatterns = [
    path('reseller/', reseller_view.resellerList),
    path('reseller/<int:id>/', reseller_view.reseller),
]
