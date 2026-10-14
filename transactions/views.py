from django.shortcuts import render
from rest_framework import viewsets

from .models import Transactions
from .serializers import TransactionSerializer


def home(request):
    return render(request, "transactions/home.html")


class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer