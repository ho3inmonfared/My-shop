from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')
    search_fields = ('first_name', 'last_name', 'phone', 'email')



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description')



@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'customer_name', 'quantity', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('product__title', 'customer__first_name', 'customer__phone')

    def product_title(self, obj):
        return obj.product.title
    
    def customer_name(self, obj):
        return f"{obj.customer.first_name} {obj.customer.last_name}"
