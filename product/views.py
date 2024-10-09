from django.shortcuts import render

from product.models import Product


# Create your views here.

# def index(request):
#    return render(request, 'product/base.html')

def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/base.html', context)