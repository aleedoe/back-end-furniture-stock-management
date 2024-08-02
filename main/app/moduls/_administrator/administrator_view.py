from rest_framework.decorators import api_view

from . import administrator_controller

@api_view(['GET', 'POST'])
def administratorList(request):
    if request.method == 'GET':
        return administrator_controller.getAllAdministrators(request)
    
    # elif request.method == 'POST':