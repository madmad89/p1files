from django.shortcuts import render
from .models import Image, Service, Product


def home(request):
    images = Image.objects.all()
    services = Service.objects.all()
    products = Product.objects.filter(available=True)
    return render(request, 'home.html', {'images': images, 'services': services, 'products': products})


def service_detail(request, id):
    service = Service.objects.get(id=id)
    return render(request, 'service_detail.html', {'service': service})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': product})
