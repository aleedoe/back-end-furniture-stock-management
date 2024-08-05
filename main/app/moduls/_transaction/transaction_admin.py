from django.contrib import admin

from . import transaction_model
admin.site.register(transaction_model.Transaction)
admin.site.register(transaction_model.TransactionDetail)
