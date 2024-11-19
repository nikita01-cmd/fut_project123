
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.product, name='catalog'),
    path('product/<int:product_id>/', views.product_one, name='product_one'),
    path('basket/', views.basket, name='basket'),
    path('basket/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
   
]   