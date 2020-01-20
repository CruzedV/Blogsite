from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import redirect

def redirect_homepage(request):
    return redirect('homepage_url', permanent=True)