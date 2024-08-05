from django.urls import path

from . import transaction_view

urlpatterns = [
    path('transaction/', transaction_view.transactionList),
]
