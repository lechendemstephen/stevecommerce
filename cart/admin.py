from django.contrib import admin # type: ignore
from .models import CartItem, Cart, Order
# Register your models here.

class CartItemAdmin(admin.ModelAdmin): 
    list_display = ('cart', 'product', 'quantity')

class CartAdmin(admin.ModelAdmin): 
    list_display = ('user',)

class OrderAdmin(admin.ModelAdmin): 
    list_display = ('orders', 'card_number', 'Name_on_card', 'expiration_date', 'cvv')

admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)