from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("app.moduls._administrator.administrator_url")),
]