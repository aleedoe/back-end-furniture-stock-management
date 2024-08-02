from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from . import furniture_model
from . import furniture_serializer

def getAllCategories(request):
    
    try:
        categories = furniture_model.Category.objects.all().order_by('id')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(categories, request)
        serializer = furniture_serializer.CategorySerializer(result_page, many=True)

        data_response = {
            'status': "success",
            'total_data': paginator.page.paginator.count,
            'total_pages': paginator.page.paginator.num_pages,
            'current_page': paginator.page.number,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'data': serializer.data,
        }
        
        return Response(data_response)
    
    except Exception as e:
        data_response = {
            'status': "error",
            'message': str(e),
        }
        
        return Response(data_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def getAllFurnitures(request):
    
    try:
        furnitures = furniture_model.Furniture.objects.all().order_by('id')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(furnitures, request)
        serializer = furniture_serializer.FurnitureSerializer(result_page, many=True)

        data_response = {
            'status': "success",
            'total_data': paginator.page.paginator.count,
            'total_pages': paginator.page.paginator.num_pages,
            'current_page': paginator.page.number,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'data': serializer.data,
        }
        
        return Response(data_response)
    
    except Exception as e:
        data_response = {
            'status': "error",
            'message': str(e),
        }
        
        return Response(data_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)