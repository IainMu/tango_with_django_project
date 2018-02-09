from django.conf.urls import url
from rango import views
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


LOGIN_URL = '/rango/login/'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$',views.add_category,name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',views.add_page,name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category,name='show_category'),
    url(r'^page/(?P<page_name_slug>[\w\-]+)/$',views.show_page,name='show_page'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$',views.user_login,name='login'),
    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    ]
