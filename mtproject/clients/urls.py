from django.urls import path, include 
from .views import index, create_product, signup, ProductsViewSet
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from . import views

router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='product')


urlpatterns = [
    path("signup/", signup, name="signup"),
    path('', index, name="clients_index.html"),
    path('create_product', create_product, name="create_product"),
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')), 
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
]