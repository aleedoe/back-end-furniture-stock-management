from django.contrib import admin

from . import furniture_model
admin.site.register(furniture_model.Category)
admin.site.register(furniture_model.Furniture)
