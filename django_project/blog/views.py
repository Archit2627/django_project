from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request,'blog/main.html')

@login_required
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html')
