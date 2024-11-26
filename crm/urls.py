from django.urls import path
from . import views

urlpatterns = [
    # Клиенты
    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/edit/<int:pk>/', views.client_edit, name='client_edit'),
    path('clients/delete/<int:pk>/', views.client_delete, name='client_delete'),

    # Товары
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),

    # Покупки
    path('purchases/', views.purchase_list, name='purchase_list'),  # Список покупок
    path('purchases/create/', views.purchase_create, name='purchase_create'),
    path('purchases/edit/<int:pk>/', views.purchase_edit, name='purchase_edit'),
    path('purchases/delete/<int:pk>/', views.purchase_delete, name='purchase_delete'),
]