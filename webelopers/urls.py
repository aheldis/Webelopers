from django.conf.urls import url
from django.urls import path

from django.contrib import admin
from polls.views import logout, signup, my_view, contact_us, profile, home, setting, panel, make_new_course, all_courses
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    url('logout', logout, name='logout'),
    url('signup', signup, name='signup'),
    url('login', my_view, name='login'),
    url('contact_us', contact_us, name='contact_us'),
    url('profile', profile, name='profile'),
    url('setting', setting, name='setting'),
    url('panel', panel, name='panel'),
    url('make_new_course', make_new_course, name='make_new_course'),
    url('all_courses', all_courses, name='all_courses')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
