from django.db import models

class AccessRights(models.Model):
    class Meta:
        db_table = '_access_rights'
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name