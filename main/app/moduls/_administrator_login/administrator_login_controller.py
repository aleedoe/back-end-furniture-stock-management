from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q

from . import administrator_login_model
from . import administrator_login_serializer

from app.moduls._administrator.administrator_model import Administrator
from app.moduls._administrator.administrator_serializer import AdministratorSerializer

def verifyLogin(request):
    try:
        username = request.data['username']
        password = request.data['password']
        
        administrator = Administrator.objects.get(Q(name=username) | Q(email=username), password=password)
        
        serializer = AdministratorSerializer(administrator)

        data_response = {
            'status': "success",
            'data': serializer.data,
        }
        
        return Response(data_response, status=status.HTTP_200_OK)
    
    except Administrator.DoesNotExist:
        data_response = {
            'status': "error",
            'message': "Invalid username or password.",
        }
        
        return Response(data_response, status=status.HTTP_401_UNAUTHORIZED)
    
    except Exception as e:
        data_response = {
            'status': "error",
            'message': str(e),
        }
        
        return Response(data_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
