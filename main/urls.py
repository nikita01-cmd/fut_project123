
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.product, name='catalog'),
    path('product/<int:product_id>/', views.product_one, name='product_one'),
    path('basket/', views.basket, name='basket'),
    path('basket/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('basket/<int:item_id>/', views.remove_from_cart, name='remove_from_cart')
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

