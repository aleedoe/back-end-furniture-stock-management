from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from . import transaction_model
from . import transaction_serializer

def getAllTransaction(request):
    
    try:
        transactions = transaction_model.Transaction.objects.all() 
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(transactions, request)
        serializer = transaction_serializer.TransactionSerializer(result_page, many=True)

        data_response = {
            'status': "success",
            'total_data': paginator.page.paginator.count,
            'total_pages': paginator.page.paginator.num_pages,
            'current_page': paginator.page.number,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'data': serializer.data,
        }
        
        return Response(data_response, status=status.HTTP_200_OK)
    
    except Exception as e:
        data_response = {
            'status': "error",
            'message': str(e),
        }
        
        return Response(data_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)