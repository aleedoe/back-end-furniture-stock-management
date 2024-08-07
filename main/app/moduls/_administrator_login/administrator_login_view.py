from rest_framework.decorators import api_view

from . import administrator_login_controller

@api_view(['POST'])
def getLogin(request):
    return administrator_login_controller.verifyLogin(request)