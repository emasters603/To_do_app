

from django.conf.urls import include, url
from django.contrib import admin
from to_do_app import views

urlpatterns = [
    url(r'^$', views.index, name = 'index' ),
    url(r'^(?P<ID>[0-100]+)/$', views.detail, name = 'detail'),
]


