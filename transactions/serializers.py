from rest_framework import serializers
from .models import Transactions

class TransactionSerializer(serializers.ModelSerializer):
    class meta:
        model = Transactions
        fields = "__all__"