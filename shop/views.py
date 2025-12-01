from django.shortcuts import redirect, render
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

def home(request):
    
    products=Product.objects.all()
    
    return render(request,'shop/home.html',context={'products':products})

def about_us(request):
    return render(request,'shop/about_us.html',{})
    
def product_detail(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'shop/product_detail.html',{'product': product})

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request=request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "با موفقیت وارد شدید.")
            return redirect('home')
        else:
            messages.error(request, "نام کاربری یا رمز عبور اشتباه است.")
            return redirect('login')
    return render(request,'shop/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, "با موفقیت خارج شدید.")
    return redirect('home')

def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "ثبت نام با موفقیت انجام شد.")
                return redirect('home')
            else:
                messages.error(request, "خطایی در ورود خودکار پس از ثبت‌نام رخ داد. لطفاً وارد شوید.")
                return redirect('login')
        else:
            messages.error(request, "خطا در ثبت نام. لطفا اطلاعات را بررسی کنید.")
            # رندر همان صفحه با فرم شامل خطاها
            return render(request, 'shop/signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'shop/signup.html', {'form': form})