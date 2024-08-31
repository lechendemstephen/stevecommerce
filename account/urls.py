from django.urls import path # type: ignore
from . import views

urlpatterns = [
   path('account/', views.sign_up, name='signup'),
   path('account/login/', views.sign_in, name='login'),
   path('logout/', views.logout_user, name='logout'),
]
