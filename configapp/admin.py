from django.contrib import admin
from .models import Category, Product, Suppliers, Order_details, Orders

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'description')
    search_fields = ('category_name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'category', 'suppliers', 'unit_price')
    list_filter = ('category', 'suppliers')
    search_fields = ('product_name',)

@admin.register(Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'contact_name', 'phone', 'city', 'country')
    search_fields = ('company_name', 'contact_name')

@admin.register(Order_details)
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'unit_price', 'quantity')

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_date', 'required_date', 'order_dtls')
    list_filter = ('order_date',)