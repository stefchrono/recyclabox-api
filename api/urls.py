from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('product-list/', views.productList, name='product-list'),
    path('product-details/<str:pk>/', views.productDetails, name='product-details'),
    path('product-list-available/', views.productListAvailable, name='product-list-available'),
    path('product-list-soldout/', views.productListSoldOut, name='product-list-soldout'),
    path('product-register/', views.productRegister, name='product-register'),
    path('product-quantity-change/<str:pk>/<str:quantity>/', views.productQuantityChange, name='product-quantity-change'),
]
