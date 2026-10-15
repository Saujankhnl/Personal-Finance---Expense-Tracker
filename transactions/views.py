
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.authentication import SessionAuthentication


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("transactions:home")
    else:
        form = UserCreationForm()

    return render(
        request,
        "transactions/register.html",
        {"form": form},
    )


@login_required
def home(request):
    return render(request, "transactions/home.html")





class TransactionsViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_queryset(self):
        # Return only the logged-in user's transactions.
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the logged-in user.
        serializer.save(user=self.request.user)

