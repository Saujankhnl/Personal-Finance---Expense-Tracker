from django.conf import settings
from django.db import models


class Transaction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="transactions",
    )
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=10,
        choices=[
            ("income", "Income"),
            ("expense", "Expense"),
        ],
    )
    category = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title