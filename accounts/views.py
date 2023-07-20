from django.shortcuts import render,redirect
from .models import Crypto
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from blogs.models import Newsletters

def register(request):
    if request.method == 'POST':
        if request.POST.get('accepted') != None :
            username = request.POST.get('username')
            password = request.POST.get('password')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            if (password=='' or lastname=="" or firstname=="" or email=="" or username==''):
                messages.error(request,"Please complete the empty field")
                return redirect('register')
            if Crypto.objects.filter(username=username) or Crypto.objects.filter(email=email):
                messages.error(request,"This username or email already used")
                return redirect('register')
            Crypto.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
            Newsletters.objects.create(email=email)
            return redirect('login')
        else :
            messages.error(request,"Please accept condition using")
            return redirect('register')
    return render(request,'accounts/register.html')

def loginUser(request):
    logout(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if user :=authenticate(request,username=username,password=password):
            login(request,user)
            return redirect('welcome')
        else:
            messages.error(request,"Authenfication failed ")
            return redirect('login')
    return render(request,'accounts/login.html')
def log_out(request):
    logout(request)
    return redirect('login')