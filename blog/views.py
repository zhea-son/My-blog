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
    posts = Post.objects.filter(is_active=True).order_by('-id')[:3]
    active = 'home'
    return render(request, 'index.html', {'posts': posts, 'active':active})

class BlogList(View):
    
    active = 'list'
    template_name = 'bloglist.html'

    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(is_active=True) 
        return render(request, self.template_name, {'posts':posts, 'active':self.active})

    def post(self, request, *args, **kwargs):
        search_str = request.POST.get("search_str")
        posts = Post.objects.filter(title__icontains=search_str, is_active=True)
        return render(request, self.template_name, {'posts':posts, 'active':self.active})


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


class Signup(View):
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


class AddBlog(View):
    template_name = 'addblog.html'
    form_class = AddBlogform
    active = "addblog"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'active':self.active, 'form':form })

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


class EditBlog(View):
    template_name = 'editblog.html'
    form_class = AddBlogform
    

    def get(self, request, id, *args, **kwargs):
        post = Post.objects.get(id=id)
        return render(request, self.template_name, {'active':'list', 'post':post})

    def post(self, request, id, *args, **kwargs):
        post = Post.objects.get(id=id)
        form = self.form_class(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('bloglist')
        return render(request, self.template_name, {'form':form})


# def editblog(request, id):

#     post = Post.objects.get(id=id)
    
#     return render(request, 'editblog.html', {'post': post})
        




