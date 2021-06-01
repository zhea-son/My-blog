from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, User
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from .forms import Loginform, Signupform, AddBlogform
from django.contrib.auth import authenticate, login


# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-id')[:3]
    active = 'home'
    return render(request, 'index.html', {'posts': posts, 'active':active})

def bloglist(request):
    posts = Post.objects.all()
    active = 'list'
    return render(request, 'bloglist.html', {'posts':posts, 'active':active})

def post_detail(request, id):

    post = Post.objects.get(id=id)
    
    return render(request, 'post_detail.html', {'post': post})


class Login(View):
    template_name = 'Login.html'
    form_class = Loginform
    active = 'login'
    def get(self, request, *args, **kwargs):
        
        form = self.form_class()

        return render(request, self.template_name, {'active':self.active, 'form':form })
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('index')
        

        return render(request, self.template_name, {'form':form, 'active':self.active})


class signup(View):
    template_name = 'signup.html'
    form_class = Signupform
    active = "signup"

    def get(self,  request, *args, **kwargs):
        return render(request, self.template_name , {'active':self.active})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, email=email, password=password)
            authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

        return render(request, self.template_name, {'active':active, 'form':form})


class addblog(View):
    template_name = 'addblog.html'
    form_class = AddBlogform
    active = "addblog"

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name, {'active':self.active })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            post = form.save(commit=False)
            post.author = user
            post.save()
            return redirect('bloglist')
        return render(request, self.template_name, {'active':self.active, 'form':form})
    
def deleteblog(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('bloglist')



        




