from rest_framework.decorators import api_view

from . import reseller_controller

@api_view(['GET', 'POST'])
def resellerList(request):
    if request.method == 'GET':
        return reseller_controller.getAllReseller(request)