from django.shortcuts import render
from mysite import models

# Create your views here.

def index(request):
    products = models.Product.objects.all()
    print(products)
    return render(request, 'index.html', locals())


def detail(request, id = 0):
    try:
        product = models.Product.objects.get(id=id)
        images =  models.PPhoto.objects.filter(product=product)
    except:
        pass
    return render(request, 'detail.html', locals())