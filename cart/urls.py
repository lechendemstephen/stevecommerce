from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('<int:product_id>/', views.add_to_cart, name='add_cart')

    
    
]

