from django.db import models # type: ignore
from store.models import Products
from django.contrib.auth.models import User # type: ignore
# Create your models here.



class Cart(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self): 

        return self.user.username



class CartItem(models.Model): 
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_date = models.DateTimeField(auto_now_add=True)


    def __str__(self): 
        return f"{self.quantity} * {self.product.name}"
    

    def total_price(self): 
        total_price = self.quantity * self.product.price

        return total_price 
    

class Order(models.Model): 
    orders = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    card_number = models.CharField(max_length=300, null=False)
    Name_on_card = models.CharField(max_length=60, null=False)
    expiration_date = models.CharField(max_length=20)
    cvv = models.CharField(max_length=5)


    def __str__(self): 

        return self.orders