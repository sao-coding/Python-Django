from re import template
from django.template.loader import get_template
from django.shortcuts import render
# from django.http import HttpResponse
from datetime import datetime,timezone,timedelta
import random
from .models import Product
from django.http import Http404

# Create your views here.

def homepage(request):
    quotes = ["今日事，今日毕", "明日事，明日毕", "昨日事，不可追", "不积跬步，无以至千里", "不积小流，无以成江海", "知識就是力量"]
    quote = random.choice(quotes)
    return render(request, 'index.html', locals())

def about(request):
    # template = get_template('about.html')
    quotes = ["今日事，今日毕", "明日事，明日毕", "昨日事，不可追", "不积跬步，无以至千里", "不积小流，无以成江海", "知識就是力量"]
    quote = random.choice(quotes)
    return render(request, 'about.html', locals())

def list(request):
    products = Product.objects.all().order_by('-price')
    return render(request, 'list.html', locals())

def detail(request, sku):
    try:
        product = Product.objects.get(sku=sku)
    except:
        return http404()
    return render(request, 'detail.html', locals())