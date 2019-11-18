from django.http import HttpResponse

from django.shortcuts import redirect
from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def redirect_homepage(request):
    return redirect('homepage_url', permanent=True)

def homepage(request):
    is_homepage = True
    return render(request, 'blogsite/homepage.html',
                context={'is_homepage': is_homepage})

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, 
                                password='password'
                                )
            login(request, user)

            return redirect('/')
    else:
        form = UserCreationForm()
    form = UserCreationForm()
    return render(request, 'registration/register.html',
                context={'form': form})

def accounts_page(request):
    return render(request, 'blogsite/accounts_page.html')