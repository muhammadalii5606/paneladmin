from django.urls import path
from .views import (
    HomeView, CategoryProductsView,
    AddCategoryView, UpdateCategoryView, DeleteCategoryView,
    AddProductView, UpdateProductView, DeleteProductView,
    AddSuppliersView, UpdateSuppliersView, DeleteSuppliersView,
    AddOrderDetailsView, UpdateOrderDetailsView, DeleteOrderDetailsView,
    AddOrdersView, UpdateOrdersView, DeleteOrdersView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<int:pk>/', CategoryProductsView.as_view(), name='category'),
    path('add_suppliers/', AddSuppliersView.as_view(), name='add_suppliers'),

    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('add_suppliers/', AddSuppliersView.as_view(), name='add_suppliers'),
    path('add_order_details/', AddOrderDetailsView.as_view(), name='add_order_details'),
    path('add_orders/', AddOrdersView.as_view(), name='add_orders'),

    path('delete_category/<int:pk>/', DeleteCategoryView.as_view(), name='delete_category'),
    path('delete_product/<int:pk>/', DeleteProductView.as_view(), name='delete_product'),
    path('delete_suppliers/<int:pk>/', DeleteSuppliersView.as_view(), name='delete_suppliers'),
    path('delete_order_details/<int:pk>/', DeleteOrderDetailsView.as_view(), name='delete_order_details'),
    path('delete_orders/<int:pk>/', DeleteOrdersView.as_view(), name='delete_orders'),

    path('update_category/<int:pk>/', UpdateCategoryView.as_view(), name='update_category'),
    path('update_product/<int:pk>/', UpdateProductView.as_view(), name='update_product'),
    path('update_suppliers/<int:pk>/', UpdateSuppliersView.as_view(), name='update_suppliers'),
    path('update_order_details/<int:pk>/', UpdateOrderDetailsView.as_view(), name='update_order_details'),
    path('update_orders/<int:pk>/', UpdateOrdersView.as_view(), name='update_orders'),
]
