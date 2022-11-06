from django.shortcuts import render
from datetime import datetime
from .models import Tv_list, Engtv_list, Car_list
# Create your views here.


def index(request, tvno=0):
    # tv_list = [
    #     {'name': '音樂台0', 'tvcode': 'jfKfPfyJRdk'},
    #     {'name': '網路流行音樂電台', 'tvcode': 'wrYF0HX7Kzc'},
    #     {'name': '中天新聞', 'tvcode': '_QbRXRnHMVY'},
    #     {'name': '公視新聞網', 'tvcode': 'fTkozUQXmF8'},
    #     {'name': '藍井エイル - 心臓', 'tvcode': 't1JaVrN5mbk'},
    # ]
    tv_list = Tv_list.objects.all()
    now = datetime.now()
    hour = now.timetuple().tm_hour
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, "index.html", locals())


def engtv(request, tvno='0'):
    # tv_list = [{'name': 'SkyNews', 'tvcode': '99U4CH_k5F0'},
    #            {'name': 'Euro News', 'tvcode': 'F-uW_IswLh8'},
    #            {'name': 'India News', 'tvcode': 'E7dbhET6_EA'},
    #            {'name': 'CCTV', 'tvcode': 'vCDDYb_M2B4'}, ]
    tv_list = Engtv_list.objects.all()
    now = datetime.now()
    hour = now.timetuple().tm_hour
    tvno = tvno
    tv = tv_list[int(tvno)]
    return render(request, 'engtv.html', locals())


def carlist(request, maker=0):
    car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan', 'Toyota']
    car_list = [
        [],
        ['Fiesta', 'Focus', 'Modeo', 'EcoSport', 'Kuga', 'Mustang'],
        ['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
        ['Mazda3', 'Mazda5', 'Mazda6', 'CX-3', 'CX-5', 'MX-5'],
        ['Tida', 'March', 'Livina', 'Sentra', 'Teana', 'X-Trail', 'Juke', 'Murano'],
        ['Camry', 'Altis', 'Yaris', '86', 'Prius', 'Vios', 'RAV4', 'Wish']
    ]
    maker = maker
    maker_name = car_maker[maker]
    cars = car_list[maker]
    return render(request, 'carlist.html', locals())


def carprice(request, maker=0):
    # car_maker = ['Ford', 'Honda', 'Mazda']
    # car_list = [[{'model': 'Fiesta', 'price': 203500, 'qty': 5},
    #             {'model': 'Focus', 'price': 605000, 'qty': 3},
    #             {'model': 'Mustang', 'price': 900000, 'qty': 1}],
    #             [{'model': 'Fit', 'price': 450000, 'qty': 2},
    #             {'model': 'City', 'price': 150000, 'qty': 1},
    #             {'model': 'NSX', 'price': 1200000, 'qty': 12}],
    #             [{'model': 'Mazda3', 'price': 329999, 'qty': 8},
    #             {'model': 'Mazda5', 'price': 603000, 'qty': 4},
    #             {'model': 'Mazda6', 'price': 850000, 'qty': 42}]]
    car_maker = Car_list.objects.values('car_maker').distinct()
    car_list = Car_list.objects.values('car_model', 'car_price', 'car_qty').filter(car_maker=car_maker[maker]['car_maker'])
    maker = maker
    maker_name = car_maker[maker]
    cars = car_list[maker]
    print(car_maker[maker])
    return render(request, 'carprice.html', locals())
