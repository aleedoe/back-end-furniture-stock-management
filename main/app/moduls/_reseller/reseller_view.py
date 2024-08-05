from rest_framework.decorators import api_view

from . import reseller_controller

@api_view(['GET', 'POST'])
def resellerList(request):
    if request.method == 'GET':
        return reseller_controller.getAllReseller(request)


@api_view(['GET', 'DELETE', 'PUT'])
def reseller(request, id):
    if request.method == 'GET':
        return reseller_controller.getResellerById(id)
    
    # elif request.method == 'DELETE':
    #     return customers_controller.deleteCustomer(id)
    
    # elif request.method == 'PUT':
    #     return customers_controller.editCustomer(request, id)