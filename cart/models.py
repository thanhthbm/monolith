from django.db import models

from accounts.models import Customer
from books.models import Book


# Create your models here.
class Cart(models.Model):
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name='cart',
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.customer.name}"

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.book.title} x {self.quantity}"