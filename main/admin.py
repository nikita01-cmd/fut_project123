from django.contrib import admin
from .models import Product

admin.site.register(Product)

from django.contrib import admin
from .models import Order

admin.site.register(Order)

from django.contrib import admin
from .models import CartItem

admin.site.register(CartItem)

from django.contrib import admin
from .models import OrderedProduct

admin.site.register(OrderedProduct)

from django.contrib import admin
from .models import Delivery

admin.site.register(Delivery)

from django.contrib import admin
from .models import Driver

admin.site.register(Driver)