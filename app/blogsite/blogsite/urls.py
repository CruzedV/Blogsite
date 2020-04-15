from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from django.urls import include

from .views import *


urlpatterns = [
	path('', redirect_homepage),

    path('blog/', include('blog.urls')),
    path('general/', include('blog_homepage.urls')),
    path('account/admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)