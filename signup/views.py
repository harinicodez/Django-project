from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import SignUpForm, LogInForm
from .models import Blog, Bloguser
import json
from django.core.serializers import serialize 
from django.contrib.auth.models import User


# Create your views here.

def signup(request):  
    form = SignUpForm()  
    return render(request, 'signup.html', {'form': form})  #signup

def login(request):
    form = LogInForm()  
    return render(request, 'login.html', {'form': form})  #login

def home(request):
    return render(request,'home.html')

def logindata(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    print(username,password)

    try:
        querydata=Bloguser.objects.all()
    except Exception:
        print(Exception)
    sd=serialize('json', querydata)
    sd=json.loads(sd)
    print(sd)
    return render(request, 'login.html', {'data':sd})             #loginblog


def authenticationForLogin(request):
    user = authenticate(username = request.POST.get('username'), password=request.POST.get('password'))
    print(user, request.POST.get('username'), request.POST.get('password'))
    if user is not None:
        try:
            querydata=Blog.objects.all()
        except Exception:
            print(Exception)
        sd=serialize('json',querydata)
        sd=json.loads(sd)
        print(sd)
        return render(request, 'blog.html', {"data": sd} )                   #login authenticate
    else:
        return render(request, 'error.html')


def signupdata(request):
    try:
        qs =Bloguser(name = request.POST.get('name'),email_address=request.POST.get('email_address'), username=request.POST.get('username'), 
           password=request.POST.get('password'))
        qs.save()
        ud =User.objects.create_user(username=request.POST.get('username'),password=request.POST.get('password'))
        ud.save()
    except Exception:
        print(Exception)

    try:
        querydata=Blog.objects.all()
    except Exception:
        print(Exception)
    sd=serialize('json',querydata)
    sd=json.loads(sd)                                                    #signupblog
    return render(request, 'blog.html', {"data": sd} )


def myblog(request):
    try:
        querydata=Blog.objects.all()
    except Exception:
        print(Exception)
    sd=serialize('json', querydata)
    sd=json.loads(sd)
    print(sd)
    return render(request, 'blog.html', {'data': sd})

def myblogid(request, blogid):
    print(blogid)
    qd = Blog.objects.filter(pk = blogid)
    sd = serialize('json',qd)                                          #readmore
    sd = json.loads(sd)
    print(sd)
    return render(request, 'blog1.html', {"data": sd})


