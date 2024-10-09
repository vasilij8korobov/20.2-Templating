from django.shortcuts import render, get_object_or_404

from product.models import Product


# Create your views here.

# def index(request):
#    return render(request, 'product/base.html')

def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/products_list.html', context)


def products_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product/products_details.html', context)
