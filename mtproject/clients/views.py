from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products
from rest_framework import viewsets
from .serializers import ProductsSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})
    
@login_required
def index(request):
    queryset = Products.objects.filter(tenant=request.tenant)  # Adjust as needed for your tenant model
    return render(request, "clients_index.html", {"Products": Products})



@login_required  #implement authentication
def create_product(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed", status=405)
    
    name = request.POST.get("name")
    if name:
        product = Products(name=name)
        product.save()
        return redirect("clients_index.html")
    else:
        return HttpResponse("Invalid product name", status=400)


#Create DRF API endpoints
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated]  