from django.contrib import admin

from . import transaction_model
admin.site.register(transaction_model.Transaction)
