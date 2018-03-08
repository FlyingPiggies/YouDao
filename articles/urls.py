from django.conf.urls import url

from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'detail/(?P<id>\d+)',views.detail, name='detail')
]