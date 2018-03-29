from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from index.models import blogtext,aboutme
def index(request):
    blog_list = blogtext.objects.all()
    for blog in blog_list:
        blog.text=blog.text[0:200]
    return render(request, 'index.html',{'blog_list':blog_list})
def about(request):
    about = aboutme.objects.get(id=1)
    return render(request,'about.html',{'about':about})
def article(request,blog_id):
    print(blog_id)
    try:
        blog = blogtext.objects.get(id=blog_id)
        tags = blog.tags.all()
    except Exception as e:
        raise Http404
    return render(request,'article.html',{'blog':blog,'tags':tags})
def bloglist(request):
    blog_list = blogtext.objects.all()
    return render(request,'bloglist.html',{'bloglist':blog_list})