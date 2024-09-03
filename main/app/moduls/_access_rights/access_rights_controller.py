from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from . import access_rights_model
from . import access_rights_serializer

def getAllAccessRights(request):
    try:
        # Fetch all access rights and order them by id
        access_rights = access_rights_model.AccessRights.objects.all().order_by('id')
        
        # Serialize the data
        serializer = access_rights_serializer.AccessRightsSerializer(access_rights, many=True)

        # Construct the response data
        data_response = {
            'status': 'success',
            'data': serializer.data,
            'description': 'Successfully retrieved all access rights'
        }
        
        return Response(data_response, status=status.HTTP_200_OK)
    
    except Exception as e:
        # Handle any exceptions that occur
        data_response = {
            'status': 'error',
            'message': 'An error occurred while retrieving access rights',
            'details': str(e)  # Include details of the exception
        }
        
        return Response(data_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)