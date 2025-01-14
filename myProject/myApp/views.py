
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required   
from .middleware import *
from django.views.decorators.cache import never_cache

# #index
############### Redirecting to Login Page Instead ##################
# def index_view(request):
#     if not request.user.is_authenticated:
#         return redirect("login")
#     return render(request, 'index.html')

#index
############## Using login_required Decorator ##################
# @login_required(login_url='login')
# def index_view(request):
#     return render(request, 'index.html')

########### Custom middleware ############
@auth
# Use cache_page Decorator with never_cache, which tells the browser not to cache the page
@never_cache
def index_view(request):
    return render(request, 'index.html')

#register
@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html',{'form':form})

#login
@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html',{'form':form})


#logout
def logout_view(request):
    logout(request)
    return redirect('login') 