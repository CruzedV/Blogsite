from blog.views import *

from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete', PostDelete.as_view(), name = 'post_delete_url'),
    path('', posts_list, name='posts_list_url'),

    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete', TagDelete.as_view(), name='tag_delete_url'),
    path('tags/', tags_list, name='tags_list_url'),

    path('user/create/', UserCreate.as_view(), name='user_create_url'),
    path('user/<str:slug>/', UserDetail.as_view(), name='user_detail_url'),
    path('user/<str:slug>/update', UserUpdate.as_view(), name='user_update_url'),
    path('user/<str:slug>/delete', UserDelete.as_view(), name='user_delete_url'),
    path('users/', users_list, name='users_list_url'),

    path('upload/', upload_image, name='upload_page_url'),
    path('search/', search_list, name='search_page_url')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)