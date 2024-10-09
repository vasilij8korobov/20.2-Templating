from django.urls import path

from product.apps import ProductConfig
from product.views import products_list, products_details

app_name = ProductConfig.name

urlpatterns = [
    path('', products_list, name='products_list'),
    path('product/<int:pk>/', products_details, name='products_details')
    # path('admin/', admin.site.urls),
    # path('', include('product.urls', namespace='product'))
]
