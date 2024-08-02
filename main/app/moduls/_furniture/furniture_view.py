from rest_framework.decorators import api_view

from . import furniture_controller

@api_view(['GET', 'POST'])
def categoryList(request):
    if request.method == 'GET':
        return furniture_controller.getAllCategories(request)

@api_view(['GET', 'POST'])
def furnitureList(request):
    if request.method == 'GET':
        return furniture_controller.getAllFurnitures(request)