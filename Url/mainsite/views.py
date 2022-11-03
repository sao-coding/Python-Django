from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    id = 36
    html = "<html><body><a href={}>溫度轉換</a>".format(reverse('C', args=(id,)))
    return HttpResponse(html)

def about(request, id = 0):
    return HttpResponse("Hello " + str(id))

def F(request, id = 0):
    html = "<p> {}°F = {}°C</p>".format(id, int((5/9)*(id-32))) + "<a href={}>攝氏轉換</a> <= 網址超連結: 127.0.0.1:5000{}".format(reverse('C', args=(int((5/9)*(id-32)),)), reverse('C', args=(int((5/9)*(id-32)),)))
    return HttpResponse(html)

def C(request, id = 36):
    html = "<p> {}°C = {}°F</p>".format(id, int((9/5)*id+32)) + "<a href={}>華氏轉換</a> <= 網址超連結: 127.0.0.1:5000{}".format(reverse('F', args=(int((9/5)*id+32),)), reverse('F', args=(int((9/5)*id+32),)))
    return HttpResponse(html)