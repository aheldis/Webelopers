from django.conf.urls import url
from django.urls import path

from django.contrib import admin
from polls.views import html_start, signup, my_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', html_start, name='html_start'),
    url('signup', signup, name='signup'),
    url('login', my_view, name='login')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
