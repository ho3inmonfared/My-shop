from django.shortcuts import render
from .models import Product

def home(request):
    
    products=Product.objects.all()
    
    return render(request,'shop/home.html',context={'products':products})

def about_us(request):
    return render(request,'shop/about_us.html',{})
    
def product_detail(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'shop/product_detail.html',{'product': product})