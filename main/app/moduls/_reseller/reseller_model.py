from django.db import models
from app.moduls._access_rights.access_rights_model import AccessRights

class Reseller(models.Model):
    class Meta:
        db_table = '_reseller'
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    access_rights_id = models.ForeignKey(AccessRights, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name