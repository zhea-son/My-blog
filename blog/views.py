from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-id')[:3]
    
    return render(request, 'index.html', {'posts': posts})

def bloglist(request):
    posts = Post.objects.all()
    return render(request, 'bloglist.html',{'posts':posts})
    