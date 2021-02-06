from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            gender = form.cleaned_data.get('gender')
            city = form.cleaned_data.get('city')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user_obj =  Profile(user = user,email = email,first_name=firstname, last_name = lastname , city = city , gender = gender)
            user_obj.save()
            messages.success(request,f'Account is created for {username}')
            return redirect('blog-home')
    else:        
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.filter(user = user)
    if profile is not None:
        print(profile)
        return render(request,'blog/profile.html',{'profiles':profile})
    return render(request,'blog/profile.html',{'user':user})