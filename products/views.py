from django.shortcuts import render
from products.models import Product

def products(request):
    theProducts = Product.objects.all()
    
    return render(request, 'products/products.html', {'products':theProducts})