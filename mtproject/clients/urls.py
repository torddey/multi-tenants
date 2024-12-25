from django.urls import path, include 
from .views import index, create_product, ProductsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='product')


urlpatterns = [
    path('', index, name="clients_index.html"),
    path('create_product', create_product, name="create_product"),
    path('api/', include(router.urls)),
]
