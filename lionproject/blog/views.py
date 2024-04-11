from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import BlogForm

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    count = len(blogs)
    return render(request, 'home.html', {'blogs':blogs,'count':count})

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog':blog,'id':id})

def new(request):
    form = BlogForm()
    return render(request,'new.html', {'form':form})

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.author = request.user
        new_blog.save()
        return redirect('detail',new_blog.id)
    return redirect('home')

def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    form = BlogForm()
    return render(request,'edit.html',{'form':form ,'blog':edit_blog})

def update(request ,id):
    
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        update_blog = form.save(commit=False)
        update_blog.pub_date = timezone.now()
        update_blog.save()
        return redirect('detail',update_blog.id)
    return redirect('home')

def delete(request , id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')