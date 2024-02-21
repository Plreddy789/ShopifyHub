
from django.db import models
from django.contrib.auth.models import User


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)

    # Add any other fields you need for the cart item, such as price, product ID, etc.

    def __str__(self):
        return f"{self.product_name} - {self.quantity} units in cart"
