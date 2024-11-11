from django.urls import path

from product.apps import ProductConfig
from product.views import ProductsListView, ProductDetailView

app_name = ProductConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='products_details')
    # path('admin/', admin.site.urls),
    # path('', include('product.urls', namespace='product'))
]
