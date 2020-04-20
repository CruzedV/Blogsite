from django.shortcuts import render

from django.views.generic import View

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from blogsite.utils import ObjectDetailMixin
from blogsite.utils import ObjectCreateMixin
from blogsite.utils import ObjectUpdateMixin
from blogsite.utils import ObjectDeleteMixin

from blog_homepage.models import News
from blog_homepage.forms import NewsForm


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
    return render(request, 'blog_homepage/homepage.html',
                context=context)

def news_and_announcement(request):
    news = News.objects.all()
    return render(request, 'blog_homepage/news_page.html',
                context={'news': news})

def register(request):
    if request.method =='POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(
                            username=username, 
                            password=password)
            login(request, user)

            return redirect('/')
    else:
        form = UserCreationForm()

    form = UserCreationForm()
    return render(request, 'registration/register.html', 
                context={'form': form})

def logout(request):
    logout(request)
    return redirect('homepage_url', permanent=True)

def accounts_page(request):
    return render(request, 'blog_homepage/accounts_page.html')
    
class NewsCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = NewsForm
    template = 'blog_homepage/news_create.html'
    raise_exception = True

class NewsDetail(LoginRequiredMixin, ObjectDetailMixin, View):
    model = News
    template = 'blog_homepage/news_detail.html'

class NewsUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = News
    form_model = NewsForm
    template = 'blog_homepage/news_update.html'
    raise_exception = True

class NewsDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = News
    template = 'blog_homepage/news_delete.html'
    redirect_url = 'news_list_url'
    raise_exception = True
