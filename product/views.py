from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from product.models import Product


class ProductsListView(ListView):
    model = Product

    #product/product_list.html


class ProductDetailView(DetailView):
    model = Product


def products_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product/product_detail.html', context)
