from django.urls import path

from product.apps import ProductConfig

app_name = ProductConfig.name

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('product.urls', namespace='product'))
]