from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def post(request):
    return render(request, 'base/post.html')

def posts(request):
    return render(request, 'base/posts.html')

def profile(request):
    return render(request, 'base/profile.html')
