from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
   # url(r'(?P<id>[a-z0-9]\w*)', views.detail, name='detail'),
