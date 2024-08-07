from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from . import administrator_login_model
from . import administrator_login_serializer

from app.moduls._administrator.administrator_model import Administrator
from app.moduls._administrator.administrator_serializer import AdministratorSerializer

def verifyLogin(data):
    try:
        administrator = Administrator.objects.get(username=data['username'], password=data['password'])
        serializer = AdministratorSerializer(many=True)

        data_response = {
            'status': "success",
            'data': serializer.data,
        }
        
        return Response(data_response, status=status.HTTP_200_OK)
    
    except Exception as e:
        data_response = {
            'status': "error",
            'message': str(e),
        }
        
        return Response(data_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)