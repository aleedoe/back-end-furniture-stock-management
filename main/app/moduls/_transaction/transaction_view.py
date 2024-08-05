from rest_framework.decorators import api_view

from . import transaction_controller

@api_view(['GET', 'POST'])
def transactionList(request):
    if request.method == 'GET':
        return transaction_controller.getAllTransaction(request)