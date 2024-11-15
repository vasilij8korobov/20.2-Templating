from django.urls import path

from product.apps import ProductConfig
from product.views import (
    ProductsListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = ProductConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='products_details'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
