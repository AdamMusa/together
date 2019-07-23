from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from accounts.models import Profile
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout

def register(request):
    form = RegisterForm()
    if request.method == 'POST' and request.FILES['image']:
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create(
                username = data['username'],
                email = data['email'],
            )

            new_user.set_password(data['password'])
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
        
            new_user.save()
            messages.success(request,'account created with succesful')
            return redirect('post:index')
    context = {
        'form':form
    }
    

    return render(request, 'accounts/register.html', context)
   

#Connexion func

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = authenticate(username=username, password=password)

            if user:
                auth_login(request, user)
                return redirect('post:index')

            
    context = {
            'form':form
        }

    return render(request, 'accounts/login.html', context)


def profileUser(request):
    user = User.objects.all()
    context = {
        'user':user
    }

    return render(request,'accounts/profile.html',context)
# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('post:index')