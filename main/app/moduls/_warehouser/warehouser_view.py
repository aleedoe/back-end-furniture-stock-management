from rest_framework.decorators import api_view

from . import warehouser_controller

@api_view(['GET', 'POST'])
def warehouserList(request):
    if request.method == 'GET':
        return warehouser_controller.getAllWarehouser(request)


@api_view(['GET', 'DELETE', 'PUT'])
def warehouser(request, id):
    if request.method == 'GET':
        return warehouser_controller.getWarehouserById(id)
    
    # elif request.method == 'DELETE':
    #     return customers_controller.deleteCustomer(id)
    
    # elif request.method == 'PUT':
    #     return customers_controller.editCustomer(request, id)