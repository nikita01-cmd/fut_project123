'''
Для приложения "Интернет магазин по продаже стойматериалов"
'''

from datetime import datetime, timedelta
# from main.models import Product, User, Order, CartItem, OrderedProduct, Delivery, Driver
from random import randint, choice
from decimal import Decimal

# Увеличим количество данных для каждого типа
NUM_PRODUCTS = 10
NUM_USERS = 5
NUM_ORDERS = 8
NUM_CART_ITEMS = 20
NUM_ORDERED_PRODUCTS = 15
NUM_DELIVERIES = 8
NUM_DRIVERS = 5

# Добавление продуктов
products = []
for i in range(NUM_PRODUCTS):
    product = Product.objects.create(
        price=Decimal(f"{randint(100, 2000)}.99"),
        category=choice(["Electronics", "Accessories", "Clothing", "Home Appliances", "Toys"]),
        type=f"Product Type {i+1}",
        weight_kg=round(randint(1, 100) / 10, 2),
        length_m=round(randint(10, 200) / 100, 2),
        width_m=round(randint(10, 100) / 100, 2),
        height_m=round(randint(5, 50) / 100, 2),
        unique_features=f"Feature {i+1}, Feature {i+2}",
        warranty_month=randint(6, 36)
    )
    products.append(product)

# Добавление пользователей
users = []
for i in range(NUM_USERS):
    user = User.objects.create(
        is_admin=choice([False]),
        is_staff=choice([False]),
        login=f"user_{i+1}",
        password="password123",
        email=f"user_{i+1}@example.com",
        name=f"User Name {i+1}",
        date_of_birth=datetime(1980 + i, randint(1, 12), randint(1, 28)),
        phone=f"12345678{randint(10, 99)}"
    )
    users.append(user)

# Добавление заказов
orders = []
for i in range(NUM_ORDERS):
    order = Order.objects.create(
        status=choice(["pending", "shipped", "delivered"]),
        payment_method=choice(["credit_card", "paypal", "cash"]),
        total_amount=Decimal(f"{randint(100, 3000)}.99"),
        user=choice(users)
    )
    orders.append(order)

# Добавление элементов корзины
cart_items = []
for i in range(NUM_CART_ITEMS):
    cart_item = CartItem.objects.create(
        user=choice(users),
        product=choice(products),
        quantity=randint(1, 5)
    )
    cart_items.append(cart_item)

# Добавление заказанных товаров
ordered_products = []
for i in range(NUM_ORDERED_PRODUCTS):
    ordered_product = OrderedProduct.objects.create(
        order=choice(orders),
        product=choice(products),
        quantity=randint(1, 3)
    )
    ordered_products.append(ordered_product)

# Добавление информации о доставке
deliveries = []
for i in range(NUM_DELIVERIES):
    delivery = Delivery.objects.create(
        order=orders[i % len(orders)],
        address=f"{randint(100, 999)} Example St, City {i+1}",
        date=datetime.now().date() + timedelta(days=randint(0, 30)),
        time=(datetime.now() + timedelta(hours=randint(8, 20))).time(),
        total_weight_kg=round(randint(10, 500) / 10, 2),
        total_volume_m3=round(randint(5, 200) / 100, 2),
        distance_from_mkad_km=round(randint(5, 50) * 1.5, 2),
        cost=Decimal(f"{randint(10, 100)}.99"),
        status=choice(["pending", "in_progress", "completed"])
    )
    deliveries.append(delivery)

# Добавление водителей
drivers = []
for i in range(NUM_DRIVERS):
    driver = Driver.objects.create(
        employee_number=f"DRV{i+1000}",
        name=f"Driver {i+1} Name",
        email=f"driver{i+1}@example.com",
        phone=f"98765432{randint(10, 99)}",
        delivery=choice(deliveries) if i < len(deliveries) else None
    )
    drivers.append(driver)

print("Данные успешно записаны в БД")
