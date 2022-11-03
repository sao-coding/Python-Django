from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def about(request, id = 0):
    return HttpResponse("Hello " + str(id))