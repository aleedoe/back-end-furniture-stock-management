from django.db import models
from app.moduls._furniture.furniture_model import Furniture

class Image(models.Model):
    class Meta:
        db_table = '_image'
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ImageContainer(models.Model):
    class Meta:
        db_table = '_image_container'
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

