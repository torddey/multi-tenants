from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products
from rest_framework import viewsets
from .serializers import ProductsSerializer

def index(request):
    products = Products.objects.all()
    return render(request, "clients_index.html", {"Products": products})

def create_product(request):
    if request.POST:
        name= request.POST.get("name")
        Product = Products(name=name)
        Product.save()
    return redirect("clients_index.html")

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer