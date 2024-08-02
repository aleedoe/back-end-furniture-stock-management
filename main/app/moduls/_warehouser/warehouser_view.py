from rest_framework.decorators import api_view

from . import warehouser_controller

@api_view(['GET', 'POST'])
def warehouserList(request):
    if request.method == 'GET':
        return warehouser_controller.getAllWarehouser(request)