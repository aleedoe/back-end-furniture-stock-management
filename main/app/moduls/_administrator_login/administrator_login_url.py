from django.urls import path

from . import administrator_login_view

urlpatterns = [
    path('admin-login/', administrator_login_view.getLogin),
]
