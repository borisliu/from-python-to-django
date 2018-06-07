from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^upload/$', views.upload),
    url(r'^output/$', views.output),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
]