from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    count = len(blogs)
    return render(request, 'home.html', {'blogs':blogs,'count':count})

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    return render(request,'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('detail',new_blog.id)