from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:pk>/', category, name='category'),
    path('add_category/', add_category, name='add_category'),
    path('add_product/', add_product, name='add_product'),
    path('add_suppliers/', add_suppliers, name='add_suppliers'),
    path('add_order_details/', add_order_details, name='add_order_details'),
    path('add_orders/', add_orders, name='add_orders'),


    path('delete_category/<int:pk>/', delete_category, name='delete_category'),
    path('delete_product/<int:pk>/', delete_product, name='delete_product'),
    path('delete_suppliers/<int:pk>/', delete_suppliers, name='delete_suppliers'),
    path('delete_order_details/<int:pk>/', delete_order_details, name='delete_order_details'),
    path('delete_orders/<int:pk>/', delete_orders, name='delete_orders'),
]
