from django.contrib import admin

from . import image_model
admin.site.register(image_model.ImageContainer)
admin.site.register(image_model.Image)
