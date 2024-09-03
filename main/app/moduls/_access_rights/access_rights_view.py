from rest_framework.decorators import api_view

from . import access_rights_controller

@api_view(['GET', 'POST'])
def accessRightList(request):
    if request.method == 'GET':
        return access_rights_controller.getAllAccessRights(request)