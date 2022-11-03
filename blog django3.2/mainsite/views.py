from django.template.loader import get_template
from django.shortcuts import redirect
from django.http import HttpResponse
from datetime import datetime,timezone,timedelta
from .models import Post

# Create your views here.

def homepage(request):
    # posts = Post.objects.all()
    # posts_list = list()
    # for count, post in enumerate(posts):
    #     print(post.created_at.astimezone(timezone(timedelta(hours=8))))
    #     posts_list.append("No.{}:".format(str(count)) + str(post) + "<br>")
    #     posts_list.append("<small>" + str(post.created_at.astimezone(timezone(timedelta(hours=8)))) + "</small><br><br>")
    #     posts_list.append("<small>" + str(post.body) + "</small><br><br>")
    # return HttpResponse(posts_list)
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')