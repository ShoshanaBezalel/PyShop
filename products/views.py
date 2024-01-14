from django.http import  HttpResponse
from django.shortcuts import render
from .models import Product

# /products -> index
# URL = Unifrom Resource Locator (Address)

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('Hi! I am the products/new page!😯 How COOL~~~')


