from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')

def catalog(request):
    return render(request, 'main/catalog.html')