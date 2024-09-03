from django.urls import path

from . import access_rights_view

urlpatterns = [
    path('access-rights/', access_rights_view.accessRightList),
]
