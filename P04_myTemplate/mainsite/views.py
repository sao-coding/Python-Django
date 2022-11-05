from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, "index.html", {'msg': 'Hello World!'})

def yt(request, tvno = 0):
    tv_list = [
        {'name':'音樂台0', 'tvcode':'jfKfPfyJRdk'},
        {'name':'網路流行音樂電台', 'tvcode':'wrYF0HX7Kzc'},
        {'name':'中天新聞', 'tvcode':'_QbRXRnHMVY'},
        {'name':'公視新聞網', 'tvcode':'fTkozUQXmF8'},
        {'name':'藍井エイル - 心臓', 'tvcode':'t1JaVrN5mbk'},
        ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, "tv.html", locals())