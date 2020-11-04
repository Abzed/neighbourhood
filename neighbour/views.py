from django.contrib.auth import login, authenticate
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.http  import HttpResponse
import datetime as dt
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout

@login_required
def index(request):
    hood_user = request.user
    user = hood_user.profile.neighbourhood.pk
    hood = get_object_or_404(Neighbourhood, pk=user)
    post = Post.objects.filter(neighbourhood=hood).order_by('-date')
    
    return render(request, 'index.html', {'hood':hood, 'post':post})

def profile(request):
    return render(request, 'profile/profile.html')

def business(request):
    hood_user = request.user
    user = hood_user.profile.neighbourhood.pk
    hood = get_object_or_404(Neighbourhood, pk=user)
    jobs = Business.objects.filter(neighbourhood=hood)
    return render(request, 'business.html', {'hood':hood, 'jobs':jobs})

@login_required
def post_news(request):
    userX = request.user
    user = Profile.objects.get(user=request.user)
    hood = Neighbourhood.objects.get(profile=user)
    
    if request.method == "POST":
        
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            data = form.save(commit=False)
            data.profile = user
            data.neighbourhood = hood
            data.save()
            return redirect('/')
        else:
            return False
    
    return render(request, 'post.html', {'form':PostForm})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        form_n = NeighbourhoodForm(request.POST)
        if form.is_valid() and form_n.is_valid():
            hood = form_n.save()               
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.bio = form.cleaned_data.get('bio')           
            user.profile.avatar = form.cleaned_data.get('avatar')
            user.profile.neighbourhood = hood
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
        form_n = NeighbourhoodForm()
    return render(request, 'signup.html', {'form': SignUpForm, 'form_n': NeighbourhoodForm})

def signin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(request,'/')
    
    return render(request, 'registration/login.html')

@login_required
def logout(request):
    django_logout(request)
    return  HttpResponseRedirect('/')