from django.urls import path # type: ignore
from . import views
urlpatterns = [
    path('', views.store, name='store' ), 
    path('about/', views.about, name='about'), 
    path('<slug:category_name>/<slug:product_slug>/', views.single_product, name='single_product')
]
