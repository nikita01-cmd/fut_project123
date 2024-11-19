from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Product, CartItem


def home(request):
    return render(request, 'main/home.html')

def catalog(request):
    return render(request, 'main/catalog.html')



def product(request):
    mydata = Product.objects.all()
    template = loader.get_template('main/catalog.html')
    products = {
        'products': mydata,
    }
    return HttpResponse(template.render(products, request))


def product_one(request, product_id):
    mydata = get_object_or_404 (Product, id=product_id)
    template = loader.get_template('main/product.html')
    context = {
        'product': mydata,
    }
  
    return HttpResponse(template.render(context, request))


def basket(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'main/basket.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    mydata = Product.objects.get(id=product_id)
    print(mydata)
    cart_item, created = CartItem.objects.get_or_create(mydata=mydata, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    print(mydata)
    return redirect('basket')