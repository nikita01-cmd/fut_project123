'''
Для приложения "Интернет магазин по продаже стойматериалов"
'''


from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Модель для товара
class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=32) 
    type = models.CharField(max_length=128)
    weight_kg = models.FloatField()
    length_m = models.FloatField()
    width_m = models.FloatField()
    height_m = models.FloatField()
    image = models.ImageField(upload_to='product_images/', blank=True)
    unique_features = models.TextField(null=True, blank=True)
    warranty_month = models.PositiveIntegerField()

    # def __str__(self):
    #     return self.type

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"



   

# Модель для заказа
class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')])
    payment_method = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order #{self.pk}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

# Модель для элементов корзины
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product}"

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"

# Модель для заказанных товаров
class OrderedProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='ordered_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product}"

    class Meta:
        verbose_name = "Ordered Product"
        verbose_name_plural = "Ordered Products"

# Модель для доставки
class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    total_weight_kg = models.FloatField()
    total_volume_m3 = models.FloatField()
    distance_from_mkad_km = models.FloatField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')])

    def __str__(self):
        return f"Delivery for Order #{self.order.pk}"

    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"

# Модель для водителя
class Driver(models.Model):
    employee_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL, null=True, blank=True, related_name='drivers')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"
