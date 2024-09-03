from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from . import administrator_controller

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def administratorList(request):
    if request.method == 'GET':
        return administrator_controller.getAllAdministrators(request)
    
    elif request.method == 'POST':
        return administrator_controller.addAdministrator(request)


@api_view(['GET', 'DELETE', 'PUT'])
def administrator(request, id):
    if request.method == 'GET':
        return administrator_controller.getAdministratorById(id)
    
    # elif request.method == 'DELETE':
    #     return customers_controller.deleteCustomer(id)
    
    # elif request.method == 'PUT':
    #     return customers_controller.editCustomer(request, id)