from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(f"<h1>{request.tenant} Index</h1>")

