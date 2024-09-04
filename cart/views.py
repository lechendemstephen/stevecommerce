from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .models import Cart
from store.models import Products
from cart.models import Cart, CartItem
from django.contrib.auth.decorators import login_required # type: ignore
# Create your views here.

@login_required(login_url='login')
def cart_view(request): 
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    items = cart.cartitem_set.all()

    context = {
        'cart': cart,
        'items': items
    }

    return render(request, 'stevecommerce/pages/cart.html', context)


@login_required(login_url='login')
def add_to_cart(request, product_id): 
    product = get_object_or_404(Products, id=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created: 
        cartitem.quantity += 1 
    cartitem.save()
    return redirect('store')
