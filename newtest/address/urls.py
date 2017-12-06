from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^page(?P<page>[0-9]+)/$', views.IndexView.as_view(), name='index'),
    url(r'^upload/$', views.upload),
    url(r'^output/$', views.output),
]