from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product


def home(request):
    return render(request, 'main/home.html')

def catalog(request):
    return render(request, 'main/catalog.html')



def product(request):
    mydata = Product.objects.all()
    template = loader.get_template('catalog.html')
    products = {
        'derevz': mydata,
    }
    return HttpResponse(template.render(products, request))