from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from . import administrator_model
from . import administrator_serializer

def getAllAdministrators(request):
    
    try:
        administrators = administrator_model.Administrator.objects.all().order_by('id')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(administrators, request)
        serializer = administrator_serializer.AdministratorSerializer(result_page, many=True)

        data_response = {
            'status': "success",
            'total_data': paginator.page.paginator.count,
            'total_pages': paginator.page.paginator.num_pages,
            'current_page': paginator.page.number,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'data': serializer.data,
            'description': 'successfully retrieve all Administrators'
        }
        
        return Response(data_response, status=status.HTTP_200_OK)
    
    except Exception as e:
        data_response = {
            'status': "error",
            'message': str(e),
        }
        
        return Response(data_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def getAdministratorById(id):
    try:
        administrator = administrator_model.Administrator.objects.get(id=id)
        serializer = administrator_serializer.AdministratorSerializer(administrator)
        
        data_response = {
            'status': 'success',
            'data': serializer.data,
            'description': 'successfully retrieve Administrator'
        }
        
        return Response(data_response, status=status.HTTP_200_OK)

    except Exception as e:
        data_response = {
            'status': 'error',
            'message': str(e)
        }
        
        return Response(data_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def addAdministrator(request):
    try:
        serializer = administrator_serializer.ActionAdministratorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data_response = {
                'status': 'success',
                'data': serializer.data,
                'description': 'Administrator created successfully'
            }
            
            return Response(data_response, status=status.HTTP_201_CREATED)
        
        data_response = {
            'status': 'error',
            'message': serializer.errors
        }
        
        return Response(data_response, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        data_response = {
            'status': 'error',
            'message': str(e)
        }
        
        return Response(data_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def updateAdministrator(request, id):
    try:
        administrator = administrator_model.Administrator.objects.get(id=id)
        serializer = administrator_serializer.ActionAdministratorSerializer(administrator, data=request.data, partial=True)

        if serializer.is_valid():
            # Membandingkan data yang ada di database dengan data yang diterima dari request
            data_is_different = False
            for field, value in serializer.validated_data.items():
                if getattr(administrator, field) != value:
                    data_is_different = True
                    break

            if data_is_different:
                serializer.save()
                data_response = {
                    'status': 'success',
                    'data': serializer.data,
                    'description': 'Administrator updated successfully'
                }
                return Response(data_response, status=status.HTTP_200_OK)
            else:
                data_response = {
                    'status': 'success',
                    'description': 'No changes detected; Administrator not updated'
                }
                return Response(data_response, status=status.HTTP_200_OK)
        else:
            data_response = {
                'status': 'error',
                'message': serializer.errors
            }
            return Response(data_response, status=status.HTTP_400_BAD_REQUEST)

    except administrator_model.Administrator.DoesNotExist:
        data_response = {
            'status': 'error',
            'message': 'Administrator not found'
        }
        return Response(data_response, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        data_response = {
            'status': 'error',
            'message': str(e)
        }
        return Response(data_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
