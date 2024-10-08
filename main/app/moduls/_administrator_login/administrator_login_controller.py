from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q

from . import administrator_login_model
from . import administrator_login_serializer

from app.moduls._administrator.administrator_model import Administrator
from app.moduls._administrator.administrator_serializer import AdministratorSerializer

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def verifyLogin(request):
    try:
        username = request.data['username']
        password = request.data['password']

        # Cek apakah ada administrator dengan username atau email yang diberikan
        try:
            administrator = Administrator.objects.get(Q(name=username) | Q(email=username))
        except Administrator.DoesNotExist:
            data_response = {
                'status': "error",
                'message': "Username not found.",
            }
            return Response(data_response, status=status.HTTP_401_UNAUTHORIZED)
        
        # Verifikasi password
        if administrator.password != password:
            data_response = {
                'status': "error",
                'message': "Invalid password.",
            }
            return Response(data_response, status=status.HTTP_401_UNAUTHORIZED)
        
        # Jika username dan password valid
        serializer = AdministratorSerializer(administrator)
        tokens = get_tokens_for_user(administrator)
        data_response = {
            'status': "success",
            'data': serializer.data,
            'tokens': tokens,
        }
        return Response(data_response, status=status.HTTP_200_OK)

    except Exception as e:
        data_response = {
            'status': "error",
            'message': str(e),
        }
        return Response(data_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
