
from django.conf.urls import include, url
from django.contrib import admin

from app01 import views

urlpatterns = [
    url(r'^set_redis$', views.set_redis),
    url(r'^get_redis$', views.get_redis),
]
