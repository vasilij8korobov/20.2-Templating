from django.urls import path

from product.apps import ProductConfig
from product.views import index

app_name = ProductConfig.name

urlpatterns = [
    path('', index)
    # path('admin/', admin.site.urls),
    # path('', include('product.urls', namespace='product'))
]