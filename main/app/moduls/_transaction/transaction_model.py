from django.db import models
from enum import Enum
from app.moduls._reseller.reseller_model import Reseller
from app.moduls._furniture.furniture_model import Furniture

class TransactionStatus(Enum):
    PENDING = 'pending'
    PROCESSED = 'processed'
    COMPLETED = 'completed'
    CANCELED = 'canceled'

class Transaction(models.Model):
    class Meta:
        db_table = '_transaction'
    reseller = models.ForeignKey(Reseller, on_delete=models.CASCADE)
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=50, choices=[(status.name, status.value) for status in TransactionStatus])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
