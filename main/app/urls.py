from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("app.moduls._administrator.administrator_url")),
    path("", include("app.moduls._reseller.reseller_url")),
    path("", include("app.moduls._warehouser.warehouser_url")),
    path("", include("app.moduls._furniture.furniture_url")),
    path("", include("app.moduls._transaction.transaction_url")),
]