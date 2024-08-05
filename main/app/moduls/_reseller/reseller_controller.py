from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from . import reseller_model
from . import reseller_serializer

def getAllReseller(request):
    
    try:
        resellers = reseller_model.Reseller.objects.all().order_by('id')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(resellers, request)
        serializer = reseller_serializer.ResellerSerializer(result_page, many=True)

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


def getResellerById(id):
    try:
        reseller = reseller_model.Reseller.objects.get(id=id)
        serializer = reseller_serializer.ResellerSerializer(reseller)
        
        data_response = {
            'status': 'success',
            'data': serializer.data
        }
        
        return Response(data_response, status=status.HTTP_200_OK)

    except Exception as e:
        data_response = {
            'status': 'error',
            'message': str(e)
        }
        
        return Response(data_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)