from django.urls import path

from product.apps import ProductConfig
from product.views import products_list

app_name = ProductConfig.name

urlpatterns = [
    path('', products_list)
    # path('admin/', admin.site.urls),
    # path('', include('product.urls', namespace='product'))
]