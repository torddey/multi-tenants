from django.shortcuts import render
from django.http import HttpResponse 

# A basic view for tenants
def index(request):
    return HttpResponse("<h1>Public Index</h1>")
