from django.shortcuts import render
from datetime import datetime

# Create your views here.


def index(request, tvno=0):
    tv_list = [
        {'name': '音樂台0', 'tvcode': 'jfKfPfyJRdk'},
        {'name': '網路流行音樂電台', 'tvcode': 'wrYF0HX7Kzc'},
        {'name': '中天新聞', 'tvcode': '_QbRXRnHMVY'},
        {'name': '公視新聞網', 'tvcode': 'fTkozUQXmF8'},
        {'name': '藍井エイル - 心臓', 'tvcode': 't1JaVrN5mbk'},
    ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, "index.html", locals())

def engtv(request, tvno='0'):
    tv_list = [{'name': 'SkyNews', 'tvcode': '99U4CH_k5F0'},
            {'name': 'Euro News', 'tvcode': 'F-uW_IswLh8'},
            {'name': 'India News', 'tvcode': 'E7dbhET6_EA'},
            {'name': 'CCTV', 'tvcode': 'vCDDYb_M2B4'}, ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[int(tvno)]
    return render(request, 'engtv.html', locals())
