from django.shortcuts import render, redirect # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
# Create your views here.

def sign_up(request): 
    if request.method == "POST": 
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['password2']
        if password == confirm_password: 
            user = User.objects.create(
                username=username,
                email=email,
                password=password
            )
            user.save()
            # authenticating user 
            user = authenticate(
                username = username,
                password = password
            )
            if user is not None: 
               login(request, user)
               return redirect('store')
            
                

        else:
            messages.error(request, 'password do not match')



    return render(request, 'stevecommerce/pages/signup.html')



def sign_in(request): 


    return render(request, 'stevecommerce/pages/login.html')

def logout_user(request): 
    logout(request)

    return redirect('store')
