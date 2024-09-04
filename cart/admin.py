from django.contrib import admin # type: ignore
from .models import CartItem, Cart
# Register your models here.

class CartItemAdmin(admin.ModelAdmin): 
    list_display = ('cart', 'product', 'quantity')

class CartAdmin(admin.ModelAdmin): 
    list_display = ('user',)

admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart, CartAdmin)
