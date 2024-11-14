from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from product.models import Product


class ProductsListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'photo', 'category', 'purchase_price')
    success_url = reverse_lazy('product:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'photo', 'category', 'purchase_price')
    success_url = reverse_lazy('product:products_list')

    def get_success_url(self):
        return reverse('product:products_details', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product:products_list')