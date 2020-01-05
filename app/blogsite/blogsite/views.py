from django.http import HttpResponse

from django.shortcuts import redirect
from django.shortcuts import render

from django.views.generic import View

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from blog.models import News

from blog.utils import ObjectDetailMixin
from blog.utils import ObjectCreateMixin
from blog.utils import ObjectUpdateMixin
from blog.utils import ObjectDeleteMixin


from blog.forms import NewsForm

from django.contrib.auth.mixins import LoginRequiredMixin


def redirect_homepage(request):
    return redirect('homepage_url', permanent=True)

def get_short():
    news = News.objects.all()[:2]
    return news

def homepage(request):
    is_homepage = True
    short_news = get_short()
    context = {
        'is_homepage': is_homepage,
        'short_news': short_news

    }
    return render(request, 'blogsite/homepage.html',
                context=context)

def register(request):
    if request.method =='POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, 
                                password=password
                                )
            login(request, user)

            return redirect('/')
    else:
        form = UserCreationForm()

    form = UserCreationForm()
    return render(request, 'registration/register.html',
                context={'form': form})

def logout(request):
    logout(request)
    return redirect('/')


def accounts_page(request):
    return render(request, 'blogsite/accounts_page.html')

def news_and_announcement(request):
    news = News.objects.all()
    return render(request, 'blogsite/news_page.html',
                context={'news': news})


class NewsCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = NewsForm
    template = 'blogsite/news_create.html'
    raise_exception = True

class NewsDetail(LoginRequiredMixin, ObjectDetailMixin, View):
    model = News
    template = 'blogsite/news_detail.html'

class NewsUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = News
    form_model = NewsForm
    template = 'blogsite/news_update.html'
    raise_exception = True

class NewsDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = News
    template = 'blogsite/news_delete.html'
    redirect_url = 'news_list_url'
    raise_exception = True