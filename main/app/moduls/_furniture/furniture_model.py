from django.db import models
from app.moduls._warehouser.warehouser_model import Warehouser

class Category(models.Model):
    class Meta:
        db_table = '_category'
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Furniture(models.Model):
    class Meta:
        db_table = '_furniture'
    name = models.CharField(max_length=255)
    prize = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    attributes = models.JSONField(null=True, blank=True)
    warehouser = models.ForeignKey(Warehouser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name