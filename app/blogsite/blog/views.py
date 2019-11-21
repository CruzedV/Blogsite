from django.core.paginator import Paginator

from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.urls import reverse

from blog.models import Tag
from blog.models import Post
from blog.models import User

from blog.utils import ObjectDetailMixin
from blog.utils import ObjectCreateMixin
from blog.utils import ObjectUpdateMixin
from blog.utils import ObjectDeleteMixin

from blog.forms import TagForm
from blog.forms import PostForm
from blog.forms import UserForm

from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin

class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update.html'
    raise_exception = True

class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'posts_list_url'
    raise_exception = True

class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'
    raise_exception = True

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update.html'
    raise_exception = True

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'posts_list_url'
    raise_exception = True

class UserCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = UserForm
    template = 'blog/user_create.html'
    raise_exception = True

class UserDetail(ObjectDetailMixin, View):
    model = User
    template = 'blog/user_detail.html'

class UserUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = User
    form_model = UserForm
    template = 'blog/user_update.html'
    raise_exception = True

class UserDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = User
    template = 'blog/user_delete.html'
    redirect_url = 'posts_list_url'
    raise_exception = True

def search_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(title__icontains=search_query)                           
    elif not search_query:
        posts = Post.objects.all()
    search_name = search_query
    context = {
            'search': posts,
            'search_name': search_name
            }
    return render(request, 'blog/search.html',
                context=context)

def posts_list(request):
    posts = Post.objects.all()
    paginated_list = paginator_for_obj(request, posts)
    next_url = paginated_list[0]
    prev_url = paginated_list[1]
    is_paginated = paginated_list[2]
    page = paginated_list[3]
    context = {
            'next_url': next_url,
            'prev_url': prev_url,
            'is_paginated': is_paginated,
            'page_object': page

    }
    return render(request, 'blog/index.html', 
                context=context)

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', 
                context={'tags': tags})

def users_list(request):
    users = User.objects.all()
    return render(request, 'blog/users_list.html',
                context={'users': users})

def paginator_for_obj(request, obj):
    paginator = Paginator(obj, 3)
    obj_number = request.GET.get('page', 1)
    page = paginator.get_page(obj_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    pag_list = (next_url, prev_url, is_paginated, page)
    return pag_list