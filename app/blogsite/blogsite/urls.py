"""blogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from .views import *

from django.contrib import admin

from django.urls import path
from django.urls import include

urlpatterns = [
	path('', redirect_homepage),
    
    path('homepage/', homepage, name='homepage_url'),

    path('blog/', include('blog.urls')),

    path('accounts/', accounts_page, name='accounts_page_url'),
    path('account/', include('django.contrib.auth.urls')),
    path('account/logout/', logout),
    path('account/register/', register, name='register_url'),
    path('account/admin/', admin.site.urls),

    path('news/create/', NewsCreate.as_view(), name='news_create_url'),
    path('news/<str:slug>/', NewsDetail.as_view(), name='news_detail_url'),
    path('news/<str:slug>/update', NewsUpdate.as_view(), name='news_update_url'),
    path('news/<str:slug>/delete', NewsDelete.as_view(), name='news_delete_url'),
    path('news/', news_and_announcement, name='news_list_url')
]