from .views import *

from django.urls import path
from django.urls import include

urlpatterns = [
    path('', homepage, name='homepage_url'),

    path('accounts/', accounts_page, name='accounts_page_url'),
    path('account/', include('django.contrib.auth.urls')),
    path('account/logout/', logout, name='logout_url'),
    path('account/register/', register, name='register_url'),

    
    path('news/create/', NewsCreate.as_view(), name='news_create_url'),
    path('news/<str:slug>/', NewsDetail.as_view(), name='news_detail_url'),
    path('news/<str:slug>/update', NewsUpdate.as_view(), name='news_update_url'),
    path('news/<str:slug>/delete', NewsDelete.as_view(), name='news_delete_url'),
    path('news/', news_and_announcement, name='news_list_url')
]