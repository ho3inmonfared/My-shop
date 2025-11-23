from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.utils.text import slugify

class Category(models.Model):
    
    title=models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    
    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    phone=models.CharField(max_length=20,validators=[MinLengthValidator(10)],unique=True)
    email=models.EmailField(max_length=300,unique=True)
    password=models.CharField(max_length=50,validators=[MinLengthValidator(8)])
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Product(models.Model):
    
    title=models.CharField(max_length=100,unique=True)
    description=models.TextField(default='')
    price=models.DecimalField(max_digits=11,decimal_places=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product/')
    created_at=models.DateTimeField(auto_now_add=True)
    
        
    def __str__(self):
        return self.title
    
class Order(models.Model):
    
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    address=models.CharField(default='',max_length=500)
    phone=models.CharField(max_length=20)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.title} = {self.quantity}"
    
    
    
